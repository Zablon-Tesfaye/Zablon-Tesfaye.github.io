# Zablon Tesfaye — Personal portfolio

A quiet, typography-led portfolio: https://zablon-tesfaye.github.io/

## Approach

The site uses a limited black/gray/warm-white palette, a simple editorial grid, and direct writing. Its layout is intentionally understated: no gradients, glass effects, decorative cards, animated counters, or external fonts.

## Structure

- `index.html` — selected projects, experience, background, and contact
- `contacts.html` — secondary contact page in the same visual language
- `portfolio.css` — active shared responsive typography and layout
- `style.css` — older stylesheet kept for reference
- `script.js` — automatically updates copyright year
- `favicon.svg` — compact neutral monogram
- `autonomous-car.svg` — original top-down line drawing of an autonomous research car
- `autonomy.css` — fixed road rail, subtle idle steering, responsive/reduced-motion behavior
- `autonomy.js` — maps scroll position to reversible car movement using animation frames
- `tests/test_site.py` — built-in Python checks for anchors, link safety, unique IDs, and required assets
- `.github/workflows/portfolio-checks.yml` — tests on pushes and pull requests
- `sitemap.xml` — public page discovery for search crawlers
- `robots.txt` — allows indexing and points crawlers to the sitemap

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

## Maintenance checks

New commits run the standard-library HTML and asset checks through GitHub Actions. The checks also validate cross-page section links, URL schemes, unique IDs, sitemap/SVG syntax, and static asset references. The fixed-side animation only performs its scroll calculations on desktop, and active section links use IntersectionObserver rather than expensive continuous layout reads. Pages stay text-first and intentionally avoid analytics, third-party scripts, or external fonts.

For printouts, the portfolio includes source URLs beside its project links. The navigation highlight resets when returning to the introduction, and the autonomous car disables movement work on smaller screens or when reduced motion is requested.

## Browser and layout resilience

The road animation pauses when its desktop-only panel is hidden, the viewport is too short, or the browser tab is inactive. Returning to a visible tab recalculates the car's position from the current scroll offset. Site checks also protect the experience-first section order, canonical page addresses, and basic accessibility landmarks.

## Interaction regression checks

The portfolio restores the car position when a browser tab resumes or when visitors navigate backward and forward. Section links update their current-location state after a direct hash jump, and the test suite checks that the experience-first layout and labelled sections remain intact. The design does not depend on these enhancements; the content and anchors remain usable without JavaScript.
