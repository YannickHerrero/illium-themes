# Sources: aamis

Upstream: https://github.com/vyrx-dev/omarchy-aamis-theme

Default branch inspected: `master`.
Pinned revision: `a155348baa139e36b6b0c14a038b3002638c1243` (committed 2026-05-25).

Local Winarchy adaptation; no upstream application configuration or script is executed. All repository entries at this revision are regular `100644` blobs (no symlinks, submodules or LFS pointers).

## Picker preview

- Source: `assets/homescreen.png` at the pinned revision (referenced by the pinned README as "Omarchy homescreen setup").
- URL: https://raw.githubusercontent.com/vyrx-dev/omarchy-aamis-theme/a155348baa139e36b6b0c14a038b3002638c1243/assets/homescreen.png
- Installed path: `preview.png` (renamed to follow Winarchy's preview discovery convention).
- Format/dimensions: PNG (RGBA), 1921 x 1081; 106,824 bytes.
- Source/installed SHA-256: `3915f9b86d8efe37bb41b669a073421736ad01f7dd42f4f00f23f20375c45c22`.

Copied byte-for-byte. It depicts an Omarchy desktop, not Winarchy.

Excluded README images (application screenshots or swatch, not desktop previews):

- `assets/setup.png`: PNG 2393 x 1320, SHA-256 `341ff602ac8ed361b0338690a4805a5b00cc73413337a207b7d3ab8fbb58b1c3`
- `assets/btop.png`: PNG 1918 x 1054, SHA-256 `36f3709d9eabd69bdb3ba130a11859d9b9c37f612bbf54635fe04038f93d98ef`
- `assets/pallete.png`: PNG 947 x 240, SHA-256 `c9e297613725d4620182e7eb3f99ee77ae39a0981d0f597f4232b757288c02d0`
- `assets/lazygit.png`, `assets/neovim.png`: not downloaded.
- `assets/icons/aamis-icon-transparent-bg.png`, `assets/icons/aamis-icon-with-bg.png`: standalone logos, not downloaded.

## Wallpaper

- Source: `backgrounds/wallhaven-mdjrqy.jpg` at the pinned revision.
- URL: https://raw.githubusercontent.com/vyrx-dev/omarchy-aamis-theme/a155348baa139e36b6b0c14a038b3002638c1243/backgrounds/wallhaven-mdjrqy.jpg
- Installed path: `wallpapers/wallhaven-mdjrqy.jpg`.
- Format/dimensions: JPEG (RGB), 5120 x 2880; 334,305 bytes.
- Source/installed SHA-256: `fddfb3025e77327ddff2c2bc6e24e10b431ebe35c286648ddbbad610a4aa3f1a`.

The repository contains one wallpaper; it is preserved unchanged. No resizing, cropping, re-encoding or metadata changes were applied. Pillow 11.1.0 was used only for decoding, dimensions and visual inspection. The filename points to wallhaven.cc id `mdjrqy`; the original artist and terms were not identified in the repository.

## License

- `LICENSE` (MIT, Copyright (c) 2025 Amit), copied unchanged: `f098a4110d03e159c5587488a7a74b25047b524e64987f047660a1faa490567b`

## Palette and review input SHA-256

All paths are repository files at the pinned revision:

- `README.md`: `bbdc45436f3176d65f80456caa7e78324ed653564591c1ab09025ebb7276b6cd`
- `colors.toml`: `a616a1f6198554428a65c04f1eccd26da54d19f42cbcf7f453aa07cd3d849302`
- `alacritty.toml`: `8c2051e8c1d4f775d4da0ddc15b86d896d87b81233fe32d386a84ebf4867237d`
- `ghostty.conf`: `17355c54fd578b3cc757d7243cddcd91fca99ea1945ce109e30f9ccff90d25f0`
- `kitty.conf`: `b7ca744c3571d9d4e33f58a760407b0e751fbf7a376b39d4349b51dd883c6b1b`
- `walker.css`: `e42ec82eb425882b4449ac1261a73cb005bfa65933052a20ecbcdd04c49852c5`
- `waybar.css`: `548af9be03d0cd086a34b9d2034235683f240a64f03523ea8f5f636f4d0e9a4a`
- `wofi.css`: `eb21d03a103626b1f5f6c6a9097c4f7e3d94d912b6ee7654526e7238c362e538`
- `hyprland.conf`: `bcd87f5bbc07e4118997413f95b94f368ce347499df85787a1342343330f2471`
- `hyprlock.conf`: `99a2f68f1e51aab48641bdd274e932b564f121bc6c5d711ce01c3c49292f1f64`
- `mako.ini`: `25ca21b373f3901d1a2d8f4dcb1750ac07194966e5cb7b89ff4fdd35a3de6aab`
- `swayosd.css`: `0931e728c0d3ae11fd5e76c846c710a02a44c0545f13ea58c9f252efde080af8`
- `btop.theme`: `1135ccfcdeca5904d3b5a6778866ec0226fc8eb6220bddf284164ea56d1e41cb`

`colors.toml` is the Aether-style format (accent/cursor/foreground/background/selection plus `color0..15`), not Quattro; no `mode` field and no `light.mode` file exist, so dark mode was passed explicitly. All 16 ANSI slots map exactly to Alacritty `[colors.normal]` and `[colors.bright]` in black/red/green/yellow/blue/magenta/cyan/white order, and `colors.toml`, `ghostty.conf` and `kitty.conf` define the same values. No Quattro template was needed.

The native palette was generated with the collection's `convert_palette.py` helper:

```text
--name "Aamis" --mode dark --ansi-source alacritty --overlay '#706a6a' --subtext '#cea37f'
```

The header comment was changed from draft to reviewed attribution; palette data was not otherwise modified. The mapping rationale is in README.md.

Generated `theme.toml` SHA-256: `c8f7de2f4548a1b23866bfcc119672d65b75df64a7d770bb5726d601d86c5b87`.
