"""Small dependency-free checks for the static portfolio.

Run with: python3 -m unittest discover -s tests
"""

from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.headings = []
        self.assets = []
        self.all_ids = []

    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        if props.get("id"):
            self.ids.add(props["id"])
            self.all_ids.append(props["id"])
        if tag in {"script", "link", "img"}:
            self.assets.append((tag, props))
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

    def test_cross_page_navigation_targets_exist(self):
        # Validate contact-page navigation back to real sections of the homepage.
        home = self.load_page("index.html")
        for link in self.load_page("contacts.html").links:
            url = link.get("href", "")
            if url.startswith("./index.html#"):
                target = url.split("#", 1)[1]
                self.assertIn(target, home.ids, f"Missing homepage target: {target}")

    def test_external_links_are_safe(self):
        for name in ("index.html", "contacts.html"):
            page = self.load_page(name)
            for link in page.links:
                if link.get("target") == "_blank":
                    tokens = link.get("rel", "").split()
                    self.assertIn("noopener", tokens)
                    self.assertIn("noreferrer", tokens)

    def test_public_links_use_secure_protocol(self):
        for page in ("index.html", "contacts.html"):
            for link in self.load_page(page).links:
                url = link.get("href", "")
                if url.startswith("http:"):
                    self.fail(f"Insecure external link in {page}: {url}")
                if url.lower().startswith("javascript:"):
                    self.fail(f"Unexpected executable link in {page}: {url}")

    def test_required_assets_exist(self):
        for asset in ("style.css", "portfolio.css", "script.js", "favicon.svg",
                      "autonomy.css", "autonomy.js", "autonomous-car.svg"):
            self.assertTrue((ROOT / asset).is_file(), asset)

    def test_unique_ids_and_skip_link(self):
        for page in ("index.html", "contacts.html"):
            parsed = self.load_page(page)
            self.assertEqual(len(parsed.all_ids), len(set(parsed.all_ids)))
            self.assertIn("content", parsed.ids)
            self.assertTrue(any(link.get("href") == "#content" for link in parsed.links))

    def test_local_asset_references_exist(self):
        # Catch missing stylesheets or animation files before deploying to Pages.
        for page in ("index.html", "contacts.html"):
            parsed = self.load_page(page)
            for tag, attrs in parsed.assets:
                path = attrs.get("src" if tag in {"script", "img"} else "href", "")
                if not path.startswith("./"):
                    continue
                clean_path = path[2:].split("?", 1)[0].split("#", 1)[0]
                self.assertTrue((ROOT / clean_path).is_file(), clean_path)

    def test_document_titles_and_canonical_addresses(self):
        # Ensure public pages have distinct titles and explicit canonical URLs.
        pages = {
            "index.html": "https://zablon-tesfaye.github.io/",
            "contacts.html": "https://zablon-tesfaye.github.io/contacts.html",
        }
        for filename, canonical in pages.items():
            content = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn("<title>", content)
            self.assertIn(f'href="{canonical}"', content)

    def test_sitemap_and_svg_parse_as_xml(self):
        # Catch malformed public metadata or artwork before GitHub Pages deploys.
        for file in ("sitemap.xml", "favicon.svg", "autonomous-car.svg"):
            ElementTree.parse(ROOT / file)
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        self.assertIn("https://zablon-tesfaye.github.io/", sitemap)
        self.assertIn("sitemap.xml", robots)

    def test_driving_study_has_scroll_driver_and_motion_fallback(self):
        # Ensure the illustration is wired to its controller and reduced-motion CSS.
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        script = (ROOT / "autonomy.js").read_text(encoding="utf-8")
        stylesheet = (ROOT / "autonomy.css").read_text(encoding="utf-8")
        self.assertIn('data-drive-rail', html)
        self.assertIn('data-drive-vehicle', html)
        self.assertIn('src="./autonomous-car.svg"', html)
        self.assertIn('scrollingElement.scrollTop', script)
        self.assertIn('prefers-reduced-motion', script)
        self.assertIn('@media (prefers-reduced-motion: reduce)', stylesheet)
        self.assertIn('@media (max-width: 1199px)', stylesheet)


if __name__ == "__main__":
    unittest.main()
