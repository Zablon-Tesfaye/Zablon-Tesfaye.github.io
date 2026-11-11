"""Small dependency-free checks for the static portfolio.

Run with: python3 -m unittest discover -s tests
"""

from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.headings = []

    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        if props.get("id"):
            self.ids.add(props["id"])
        if tag == "a":
            self.links.append(props)
        if tag in {"h1", "h2"}:
            self.headings.append((tag, props.get("id")))


class PortfolioChecks(unittest.TestCase):
    def load_page(self, name):
        parser = SiteParser()
        parser.feed((ROOT / name).read_text(encoding="utf-8"))
        return parser

    def test_navigation_targets_exist(self):
        page = self.load_page("index.html")
        for link in page.links:
            target = link.get("href", "")
            if target.startswith("#"):
                self.assertIn(target[1:], page.ids, f"Unresolved anchor: {target}")

    def test_page_main_and_headings_have_ids(self):
        for name in ("index.html", "contacts.html"):
            page = self.load_page(name)
            self.assertIn("content", page.ids)
            self.assertTrue(any(tag == "h1" for tag, _ in page.headings))

    def test_external_links_are_safe(self):
        for name in ("index.html", "contacts.html"):
            page = self.load_page(name)
            for link in page.links:
                if link.get("target") == "_blank":
                    tokens = link.get("rel", "").split()
                    self.assertIn("noopener", tokens)
                    self.assertIn("noreferrer", tokens)

    def test_required_assets_exist(self):
        for asset in ("style.css", "script.js", "favicon.svg"):
            self.assertTrue((ROOT / asset).is_file(), asset)


if __name__ == "__main__":
    unittest.main()
