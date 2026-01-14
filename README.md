# Arunmozhi Blog

This repository hosts the Hugo version of the blog using the Nightfall theme.

## Tech

- Hugo (extended)
- Theme: Nightfall (git submodule)

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

Nightfall is included as a submodule:

```bash
git submodule update --init --recursive
```

To update:

```bash
git submodule update --remote --merge
```

## Custom styling

- Fonts and head includes: `layouts/_partials/custom-head.html`
- Custom styles: `static/css/custom.css`

## Deployment

GitHub Actions builds and deploys to GitHub Pages on pushes to `main`:
- Workflow: `.github/workflows/gh-pages.yml`

Make sure GitHub Pages is configured to use GitHub Actions as the source.
