# Zablon Tesfaye — Portfolio

A lightweight personal portfolio hosted with GitHub Pages, featuring research, professional experience, and selected engineering projects.

**Website:** https://zablon-tesfaye.github.io/

## What's included

- `index.html` — introduction, projects, experience timeline, skills, and contact section
- `contacts.html` — accessible standalone contact page
- `style.css` — responsive layouts and a small shared design system
- `script.js` — project filters, mobile navigation, and automatic footer year
- `favicon.svg` — self-contained monogram icon

## Run locally

No build system or API keys are required. From the repository directory:

```bash
python3 -m http.server 8000
```

Open http://localhost:8000 in a browser.

## Updating content

Project details and resume-based experience are deliberately written in semantic HTML instead of loaded from a remote service. To add a project, copy a `project-card` article in `index.html` and set `data-categories` to `ai`, `systems`, or both. The filter buttons pick up the new card without changes to JavaScript.

The Legacy project is private, so its card gives an overview without implying its source repository is publicly accessible. Contact links use `mailto:` and existing profile URLs; there is no nonfunctional contact form.

## Engineering notes

- Vanilla HTML, CSS, and JavaScript; no package install or runtime dependencies.
- Responsive, keyboard-accessible navigation, visible focus states, semantic sections, and reduced-motion support.
- Comments explain why important logic exists, for example, the project filtering and mobile navigation behavior.
- Resume-derived descriptions intentionally avoid unverified benchmark numbers.

## Deployment

GitHub Pages can publish from `main` / repository root under **Settings → Pages**. The URL above assumes the standard username GitHub Pages configuration.
