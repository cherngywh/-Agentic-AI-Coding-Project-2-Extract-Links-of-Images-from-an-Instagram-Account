#!/usr/bin/env python3
"""
Collect Instagram post URLs from a profile.
Usage: python get_urls.py --use-chrome
(Requires Chrome running with --remote-debugging-port=9222, logged into Instagram)
"""
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Run: pip install playwright && playwright install chromium")
    sys.exit(1)

PROFILE_URL = "https://www.instagram.com/0_shufen/"
USE_CHROME = "--use-chrome" in sys.argv

with sync_playwright() as p:
    if USE_CHROME:
        try:
            browser = p.chromium.connect_over_cdp("http://localhost:9222")
            page = None
            for ctx in browser.contexts:
                for pg in ctx.pages:
                    if "instagram.com/0_shufen" in pg.url:
                        page = pg
                        break
                    if "instagram.com" in pg.url and page is None:
                        page = pg
                if page:
                    break
            if not page and browser.contexts and browser.contexts[0].pages:
                page = browser.contexts[0].pages[0]
            if not page:
                raise Exception("Open instagram.com/0_shufen/ in Chrome first.")
            if "instagram.com/0_shufen" not in page.url:
                page.goto(PROFILE_URL, wait_until="domcontentloaded", timeout=60000)
        except Exception as e:
            print(f"Connect failed: {e}. Run Chrome with: --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug")
            sys.exit(1)
    else:
        browser = p.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        )
        page = context.new_page()
        page.goto(PROFILE_URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(2000 if USE_CHROME else 3000)

    if not USE_CHROME and page.locator('input[name="username"]').count() > 0:
        print("\n>>> Browser is open - please log in now. Waiting 45 seconds... <<<")
        page.wait_for_timeout(45000)
        page.goto(PROFILE_URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(2000)

    print("Scrolling for 5 seconds...")
    try:
        for _ in range(10):
            page.evaluate("window.scrollBy(0, 400)")
            page.wait_for_timeout(500)
    except Exception:
        pass

    page.wait_for_timeout(1500)

    try:
        # Get post URLs - try multiple selectors for links to posts
        urls = page.evaluate("""
        () => {
            const seen = new Set();
            document.querySelectorAll('a[href*="/p/"], a[href*="instagram.com/p"]').forEach(a => {
                let href = a.getAttribute('href') || a.href || '';
                const m = href.match(/\\/p\\/([A-Za-z0-9_-]+)/);
                if (m) {
                    const url = 'https://www.instagram.com/p/' + m[1] + '/';
                    seen.add(url);
                }
            });
            if (seen.size === 0) {
                document.querySelectorAll('a').forEach(a => {
                    const h = a.href || '';
                    const m = h.match(/instagram\\.com\\/p\\/([A-Za-z0-9_-]+)/);
                    if (m) seen.add('https://www.instagram.com/p/' + m[1] + '/');
                });
            }
            return Array.from(seen);
        }
    """)
    except Exception:
        urls = []

    if not USE_CHROME:
        browser.close()

urls = list(dict.fromkeys(urls))
print(f"\nFound {len(urls)} post URLs (click to view photo):\n")
for u in urls:
    print(u)
