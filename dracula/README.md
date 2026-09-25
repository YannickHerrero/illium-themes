# Dracula — Illium

Dark theme adapted from [dracula/omarchy](https://github.com/dracula/omarchy), maintained upstream by Chris AtLee and contributors.

The background, text, selection and all 16 terminal colors come from upstream `alacritty.toml`. Illium uses normal black for its bar surface, comment/bright black for secondary text, and Dracula purple (`#bd93f9`) as its single accent. This chooses the purple endpoint of the upstream cyan/purple border treatment rather than attempting to reproduce a gradient.

Includes all three upstream wallpapers without resizing or recompression: `base.png`, `dracula-leaves-6272a4-dark.png`, and `dracula-mnt-282a36.png`.

The visual picker uses upstream `screenshot.png`, copied unchanged as `preview.png`. It is a screenshot of Omarchy, not Illium; see `SOURCES.md` for the mapping and hash.

The upstream MIT license is preserved in `LICENSE`; see `SOURCES.md` for the pinned revision and SHA-256 hashes.

Install: `illiumctl theme install <path-to-this-folder>`, then `illiumctl theme set dracula`.
