import re
import time
import os
import requests
from requests.auth import HTTPBasicAuth

AUTH = ("agent", "nJKltWqJzezM9lXFNArstS5f")
BASE = "https://dotheygobad.com/wp-json/wp/v2"
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs", "articles")
os.makedirs(OUT_DIR, exist_ok=True)

session = requests.Session()
session.auth = AUTH

def strip_html(text):
    text = re.sub(r"<h2[^>]*>", "\n\n## ", text)
    text = re.sub(r"</h2>", "\n\n", text)
    text = re.sub(r"<h3[^>]*>", "\n\n### ", text)
    text = re.sub(r"</h3>", "\n\n", text)
    text = re.sub(r"<a\s+[^>]*href=[\"']([^\"']+)[\"'][^>]*>([^<]*)</a>", r"[\2](\1)", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" +", " ", text)
    return text.strip()

def api_get(endpoint, params, retries=3):
    for attempt in range(retries):
        try:
            resp = session.get(f"{BASE}/{endpoint}", params=params, timeout=30)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code in (502, 503, 504) and attempt < retries - 1:
                print(f"  {e.response.status_code}, retrying ({attempt+2}/{retries})...", flush=True)
                time.sleep(3)
            else:
                raise
        except requests.exceptions.RequestException:
            if attempt < retries - 1:
                print(f"  connection error, retrying ({attempt+2}/{retries})...", flush=True)
                time.sleep(3)
            else:
                raise

slugs = []
for page in [1, 2]:
    data = api_get("posts", {"per_page": 100, "page": page, "_fields": "slug"})
    if not data:
        break
    slugs.extend(p["slug"] for p in data)
    print(f"[slugs] page {page}: got {len(data)} slugs (total: {len(slugs)})")

print(f"\nTotal slugs: {len(slugs)}\n")

def fetch_post(slug):
    posts = api_get("posts", {"slug": slug, "_embed": "wp:featuredmedia"})
    if not posts:
        return None
    return posts[0]

for i, slug in enumerate(slugs):
    filepath = os.path.join(OUT_DIR, f"{slug}.md")
    if os.path.exists(filepath):
        print(f"[{i+1}/{len(slugs)}] {slug} ... ALREADY EXISTS")
        continue
    print(f"[{i+1}/{len(slugs)}] fetching {slug} ...", end=" ", flush=True)
    try:
        post = fetch_post(slug)
    except Exception as e:
        print(f"ERROR: {e}")
        continue
    if post is None:
        print("SKIPPED")
        continue
    title = post["title"]["rendered"]
    content = strip_html(post["content"]["rendered"])

    frontmatter = f"---\ntitle: {title}\n---\n\n"
    filepath = os.path.join(OUT_DIR, f"{slug}.md")
    with open(filepath, "w") as f:
        f.write(frontmatter + content)

    print(f"-> {title}")
    time.sleep(1)

print("\nDone.")
