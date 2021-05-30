# texts

## About

## Deployment

```bash
pelican content -s publishconf.py
```

This deletes the output/ folder, and compiles it again. Then after pushing, there is a GitHub action that takes the output/ folder and pushes it to gh-pages for GitHub Pages.
