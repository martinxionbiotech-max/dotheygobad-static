#!/usr/bin/env python3
import requests
import html.parser
import os
import re
import sys
import time

BASE = 'https://dotheygobad.com'
API = f'{BASE}/wp-json/wp/v2'
AUTH = (os.environ.get('WP_USER', 'agent'), os.environ.get('WP_PASS', ''))
OUT_ARTICLES = 'docs/articles'
OUT_PAGES = 'docs/pages'
OUT_IMAGES = 'docs/assets/images'

os.makedirs(OUT_ARTICLES, exist_ok=True)
os.makedirs(OUT_PAGES, exist_ok=True)
os.makedirs(OUT_IMAGES, exist_ok=True)


class HTMLToMarkdown(html.parser.HTMLParser):
    """Convert WordPress post HTML into clean Markdown."""

    def __init__(self):
        super().__init__()
        self.out = []
        self._link_url = ''
        self._link_text = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('h2', 'h3', 'h4'):
            level = int(tag[1])
            self.out.append('\n\n' + '#' * level + ' ')
        elif tag in ('b', 'strong'):
            self.out.append('**')
        elif tag in ('i', 'em'):
            self.out.append('*')
        elif tag == 'a':
            self._link_url = a.get('href', '')
            self._link_text = []
        elif tag in ('br',):
            self.out.append('\n')
        elif tag in ('p', 'li', 'ul', 'ol', 'blockquote'):
            self.out.append('\n')
        elif tag == 'img':
            src = a.get('src', '')
            alt = a.get('alt', '')
            if src:
                self.out.append(f'\n![{alt}]({src})\n')

    def handle_endtag(self, tag):
        if tag in ('h2', 'h3', 'h4'):
            self.out.append('\n')
        elif tag in ('b', 'strong'):
            self.out.append('**')
        elif tag in ('i', 'em'):
            self.out.append('*')
        elif tag == 'a':
            text = ''.join(self._link_text).strip()
            url = self._link_url.strip()
            if text and text != url:
                self.out.append(f'[{text}]({url})')
            elif url:
                self.out.append(url)
            self._link_url = ''
            self._link_text = []
        elif tag in ('p', 'li', 'div'):
            self.out.append('\n')

    def handle_data(self, data):
        if self._link_url:
            self._link_text.append(data)
        else:
            self.out.append(data)

    def get(self):
        md = ''.join(self.out)
        md = re.sub(r'\n{3,}', '\n\n', md)
        md = re.sub(r'[ \t]+$', '', md, flags=re.MULTILINE)
        return md.strip()


def fetch_all_slugs(endpoint):
    """Fetch all slugs from a paginated endpoint (lightweight)."""
    slugs = []
    page = 1
    while True:
        r = requests.get(
            f'{API}/{endpoint}',
            auth=AUTH,
            params={'per_page': 100, 'page': page, '_fields': 'slug'}
        )
        r.raise_for_status()
        data = r.json()
        if not data:
            break
        slugs.extend(item['slug'] for item in data)
        print(f'  {endpoint} page {page}: {len(data)} slugs (total {len(slugs)})')
        page += 1
        if len(data) < 100:
            break
    return slugs


def fetch_item(endpoint, slug):
    """Fetch a single item by slug with embedded featured media."""
    r = requests.get(
        f'{API}/{endpoint}',
        auth=AUTH,
        params={'slug': slug, '_embed': 'wp:featuredmedia'}
    )
    r.raise_for_status()
    data = r.json()
    return data[0] if data else None


def html_to_md(html_str):
    p = HTMLToMarkdown()
    p.feed(html_str)
    return p.get()


def download_image(url, dest):
    try:
        r = requests.get(url, auth=AUTH, stream=True, timeout=30)
        r.raise_for_status()
        with open(dest, 'wb') as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        return True
    except Exception as e:
        print(f'    image failed: {e}')
        return False


def process_item(item, kind='article'):
    slug = item['slug']
    title = item['title']['rendered']
    html = item.get('content', {}).get('rendered', '')
    md_body = html_to_md(html)

    fm = f'---\ntitle: {title}\n---\n\n'
    content = fm + md_body + '\n'

    if kind == 'article':
        path = os.path.join(OUT_ARTICLES, f'{slug}.md')
    else:
        path = os.path.join(OUT_PAGES, f'{slug}.md')

    with open(path, 'w') as f:
        f.write(content)

    # featured image
    media = item.get('_embedded', {}).get('wp:featuredmedia', [])
    img_status = ''
    if media:
        img_url = media[0].get('source_url')
        if img_url:
            ext = os.path.splitext(img_url.split('?')[0])[1] or '.jpg'
            img_path = os.path.join(OUT_IMAGES, f'{slug}{ext}')
            if download_image(img_url, img_path):
                img_status = ' +img'
    print(f'  wrote {kind}/{slug}.md{img_status}')


def main():
    # Posts
    print('Fetching post slugs...')
    post_slugs = fetch_all_slugs('posts')
    print(f'Total post slugs: {len(post_slugs)}')

    print('\nFetching full posts...')
    for i, slug in enumerate(post_slugs):
        print(f'  [{i+1}/{len(post_slugs)}] {slug}')
        item = fetch_item('posts', slug)
        if item:
            process_item(item, 'article')
        else:
            print(f'    not found')
        # Rate limiting between requests
            time.sleep(0.3)  # be gentle to the server

    # Pages
    print('\nFetching page slugs...')
    page_slugs = fetch_all_slugs('pages')
    print(f'Total page slugs: {len(page_slugs)}')

    print('\nFetching full pages...')
    for i, slug in enumerate(page_slugs):
        print(f'  [{i+1}/{len(page_slugs)}] {slug}')
        item = fetch_item('pages', slug)
        if item:
            process_item(item, 'page')
        else:
            print(f'    not found')
        time.sleep(0.3)

    print('\nDone.')


if __name__ == '__main__':
    main()
