import re
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

SITEMAP_NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def _meta_date(md_path):
    text = Path(md_path).read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    try:
        meta = yaml.safe_load(text[3:end]) or {}
    except Exception:
        return None
    return meta.get("dateModified") or meta.get("date")


def _path_to_file(url_path, docs_dir):
    rel = url_path.strip("/")
    docs = Path(docs_dir)
    if not rel:
        return docs / "index.md"
    candidates = [
        docs / (rel + ".md"),
        docs / rel / "index.md",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    # Handle old-style root paths that resolve to articles/categories/legal pages.
    parts = [p for p in rel.split("/") if p]
    if parts and parts[0] in {"articles", "categories", "about", "legal"}:
        return None
    for prefix in ("articles", "categories"):
        candidate = docs / prefix / (parts[-1] + ".md")
        if candidate.exists():
            return candidate
    return None


def on_post_build(config, **kwargs):
    sitemap_path = Path(config["site_dir"]) / "sitemap.xml"
    if not sitemap_path.exists():
        return

    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    changed = 0
    for url in root.findall("s:url", SITEMAP_NS):
        loc = url.findtext("s:loc", namespaces=SITEMAP_NS)
        lastmod = url.find("s:lastmod", SITEMAP_NS)
        if loc is None or lastmod is None:
            continue

        path = loc.replace(config.get("site_url", ""), "", 1)
        if path.startswith("/"):
            path = path[1:]
        md_path = _path_to_file(path, config["docs_dir"])
        if md_path is None:
            continue
        date_value = _meta_date(md_path)
        if date_value:
            lastmod.text = str(date_value)
            changed += 1

    ET.indent(tree, space="    ")
    tree.write(sitemap_path, encoding="utf-8", xml_declaration=True)
    print(f"sitemap-hooks: rewrote {changed} lastmod values from frontmatter")
