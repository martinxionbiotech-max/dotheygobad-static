"""Emit a Markdown sidecar for every page so agents can fetch the source text.

For each page the build produces (for example /articles/foo/), this hook also
writes /articles/foo/index.md containing the page's Markdown with its YAML
frontmatter removed and a one-line provenance header added.

Why a sidecar rather than content negotiation: Cloudflare Pages serves static
files, so the response for a URL cannot depend on the Accept header without an
edge function. A parallel .md path works everywhere, caches like any other asset
and needs no runtime.

The HTML advertises the sidecar with <link rel="alternate" type="text/markdown">,
and llms.txt lists the convention.
"""

from pathlib import Path

SKIP_DIRS = {"overrides", "scripts", "hooks", "node_modules", ".git"}
SKIP_NAMES = {"llms.txt", "ads.txt"}


def _strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :].lstrip("\n")
    return text


def _sidecar_rel(md_rel: str, use_directory_urls: bool) -> str:
    """Map docs-relative path to the .md path served alongside the page."""
    if md_rel == "index.md":
        return "index.md"
    if md_rel.endswith("/index.md"):
        return md_rel[:-len("index.md")] + "index.md"
    if use_directory_urls:
        return md_rel[:-3] + "/index.md"
    return md_rel  # non-directory URLs already end in .md


def on_post_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    site_dir = Path(config["site_dir"])
    site_url = str(config.get("site_url") or "").rstrip("/")
    use_directory_urls = bool(config.get("use_directory_urls", True))

    written = 0
    for md in sorted(docs_dir.rglob("*.md")):
        rel = md.relative_to(docs_dir).as_posix()
        if any(part in SKIP_DIRS for part in md.relative_to(docs_dir).parts[:-1]):
            continue
        if md.name in SKIP_NAMES or rel.startswith("."):
            continue

        body = _strip_frontmatter(md.read_text(encoding="utf-8", errors="replace")).strip()
        if not body:
            continue

        out_rel = _sidecar_rel(rel, use_directory_urls)
        out = site_dir / out_rel
        out.parent.mkdir(parents=True, exist_ok=True)

        page_url = "/" + out_rel[: -len("index.md")] if out_rel.endswith("index.md") else "/" + out_rel
        header = f"<!-- source: {site_url}{page_url} -->\n\n" if site_url else ""
        out.write_text(header + body + "\n", encoding="utf-8")
        written += 1

    print(f"markdown-sidecars: wrote {written} .md files")
