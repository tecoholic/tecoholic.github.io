# Arunmozhi Blog

This repository hosts the Hugo version of the blog using the LoveIt theme.

## Tech

- Hugo (extended)
- Theme: LoveIt (git submodule)

## Local development

Requirements:
- Hugo extended (>= 0.146.0)
- Dart Sass (`sass` CLI)

Commands:

```bash
hugo server
```

Build:

```bash
hugo --minify
```

## Content

- Posts: `content/posts/`
- Pages: `content/`
- Static assets: `static/`

## Theme

LoveIt is included as a submodule:

```bash
git submodule update --init --recursive
```

To update:

```bash
git submodule update --remote --merge
```

## Taxonomy term pages

- Hugo v0.154+ renders tag/category term pages as kind `term` and looks for `layouts/taxonomy/term.html`.
- LoveIt ships `themes/LoveIt/layouts/taxonomy/list.html` and `themes/LoveIt/layouts/taxonomy/terms.html` but no `term.html`.
- This repo provides `layouts/taxonomy/term.html` to render HTML for `/tags/<term>/` and `/categories/<term>/`.

## Custom styling

- Dark theme overrides: `assets/css/dark-overrides.css` (wired via `params.page.library.css.darkOverrides` in `hugo.toml`).
- Light theme overrides: `assets/css/light-overrides.css` (wired via `params.page.library.css.lightOverrides` in `hugo.toml`).

## Deployment

GitHub Actions builds and deploys to GitHub Pages on pushes to `main`:
- Workflow: `.github/workflows/gh-pages.yml`

Make sure GitHub Pages is configured to use GitHub Actions as the source.
