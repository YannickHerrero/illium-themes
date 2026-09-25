# Mecha no Onna V2 — Illium

Dark warm amber/cream theme adapted from [HANCORE's Mecha no Onna](https://github.com/HANCORE-linux/omarchy-mechanoonna-theme), default V2 branch. Upstream acknowledges Aether by bjarneo.

All 16 terminal colors are preserved exactly from `alacritty.toml` (also matching `colors.toml` color0–color15). Background/bar use upstream `#1c1b19`, text `#f0e4c5`, selection `#706e6b`, accent `#d4bd99`. Secondary text uses Walker's readable `#a89984` rather than dim bright-black. Illium has one accent and opaque RGB roles: it does not reproduce Hyprland's cream-to-background border gradient, frosted glass, application opacity, blur or application-specific configuration. Its WezTerm cursor follows the amber accent rather than upstream's cream cursor.

Includes unchanged `preview.png` (an Omarchy screenshot, not an Illium live preview) and all three original JPEG wallpapers, `BG1.jpg`–`BG3.jpg`, without resizing or recompression. No scripts or application extensions are installed.

Upstream's MIT license is preserved in `LICENSE`. Artwork and depicted branding remain subject to their respective owners' rights; the repository license is not independent verification of third-party image rights. See `SOURCES.md` for the pinned revision and hashes.

Install: `illiumctl theme install <path-to-this-folder>`.
Select explicitly: `illiumctl theme set mechanoonna`, or **Alt+Shift+Space → Theme** and filter `mechanoonna`. Installation alone does not activate the theme.
