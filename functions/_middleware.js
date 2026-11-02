/**
 * Content negotiation for AI agents.
 *
 * A request with `Accept: text/markdown` against a page URL is served that page's
 * Markdown sidecar (/<page>/index.md) instead of the HTML, with
 * `Vary: Accept` on both responses so a cache never mixes the two.
 *
 * Everything else — browsers, crawlers, AdSense, static assets — passes straight
 * through untouched. If the sidecar is missing or the fetch fails, the request
 * falls back to the normal HTML response rather than erroring.
 */

const ASSET_RE = /\.(md|html?|xml|txt|json|css|js|mjs|png|jpe?g|svg|webp|gif|ico|woff2?|ttf|pdf|zip)$/i;

export async function onRequest(context) {
  const { request, env, next } = context;
  const url = new URL(request.url);
  const accept = (request.headers.get("accept") || "").toLowerCase();

  const withVary = (res) => {
    try {
      const headers = new Headers(res.headers);
      headers.set("Vary", "Accept");
      return new Response(res.body, { status: res.status, statusText: res.statusText, headers });
    } catch (_) {
      return res;
    }
  };

  if (request.method !== "GET" || !accept.includes("text/markdown") || ASSET_RE.test(url.pathname)) {
    return withVary(await next());
  }

  try {
    const base = url.pathname.replace(/\/+$/, "");
    const mdUrl = new URL(`${base}/index.md`, url.origin);
    const mdRes = await env.ASSETS.fetch(new Request(mdUrl.toString(), { method: "GET" }));

    if (mdRes.ok) {
      return new Response(await mdRes.text(), {
        status: 200,
        headers: {
          "Content-Type": "text/markdown; charset=utf-8",
          "Vary": "Accept",
          "Cache-Control": "public, max-age=300",
          "Link": `<${url.origin}${url.pathname}>; rel="canonical"`,
          "X-Markdown-Negotiated": "1",
        },
      });
    }
  } catch (_) {
    // fall through to HTML
  }

  return withVary(await next());
}
