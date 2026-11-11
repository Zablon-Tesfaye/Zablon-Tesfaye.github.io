# Zablon Tesfaye — Personal portfolio

A quiet, typography-led portfolio: https://zablon-tesfaye.github.io/

## Approach

The site uses a limited black/gray/warm-white palette, a simple editorial grid, and direct writing. Its layout is intentionally understated: no gradients, glass effects, decorative cards, animated counters, or external fonts.

## Structure

- `index.html` — selected projects, experience, background, and contact
- `contacts.html` — secondary contact page in the same visual language
- `style.css` — shared responsive typography and layout
- `script.js` — automatically updates copyright year
- `favicon.svg` — compact neutral monogram
- `tests/test_site.py` — built-in Python checks for anchors, link safety, and required assets

## Local preview

```bash
python3 -m http.server 8000
```

Visit http://localhost:8000.

## Test the site

```bash
python3 -m unittest discover -s tests -v
```

The tests use only the Python standard library, so no dependencies need to be installed. They check same-page navigation targets, essential files, and the security attributes on external links.

## Editing content

Projects are numbered HTML `article` elements within the `work-list` container. Update them directly and keep the language concise. Experience and background follow the same approach. Comments explain structural decisions rather than narrate each CSS declaration. The stylesheet also includes narrow-screen adjustments, visible keyboard focus, and a print-specific layout.

The Legacy source code is private, so the portfolio does not link to it. Resume-based experience remains descriptive rather than introducing unverified performance claims.

## Deployment

GitHub Pages publishes from the repository's `main` branch. Deployment status is visible under the repository's **Actions** tab.
