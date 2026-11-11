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
- `autonomous-car.svg` — original top-down line drawing of an autonomous research car
- `autonomy.css` — fixed road rail, subtle idle steering, responsive/reduced-motion behavior
- `autonomy.js` — maps scroll position to reversible car movement using animation frames
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

## Autonomous vehicle interaction

On desktop widths of 1200px or more, the vehicle sits on a slim fixed road at the left edge. It starts near the bottom of that road and moves upward as visitors scroll down the portfolio; scrolling back reverses the motion. A slight steering sway plays while idle. On tablets and phones, the rail is hidden to preserve reading space, and users who prefer reduced motion see a stationary car instead of animation.

The illustration is a locally hosted SVG with no image service, animation framework, or third-party dependency. The functionality is isolated so the minimalist content layout can remain unchanged.
