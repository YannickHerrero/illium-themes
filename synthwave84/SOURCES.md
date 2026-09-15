# Sources — Synthwave '84

Upstream: https://github.com/omacom/omarchy-synthwave84-theme

Default branch inspected: `master`.
Pinned revision: `283dbcf17c3a500b7d3ddfce081e1dc2b3641172`.

No LICENSE, explicit README license grant, `colors.toml` or light-mode marker is present at this revision. No upstream scripts/configuration were executed. This is a local personal adaptation, not a redistribution license (see README.md).

## Preview: external attachment referenced by the pinned README

- Referring file: https://github.com/omacom/omarchy-synthwave84-theme/blob/283dbcf17c3a500b7d3ddfce081e1dc2b3641172/README.md
- Original image URL: https://github.com/user-attachments/assets/6be31d95-57ab-4228-9cfc-a147a3cdfaf6
- Redirect origin/path: `https://github-production-user-asset-6210df.s3.amazonaws.com/2741/471149046-6be31d95-57ab-4228-9cfc-a147a3cdfaf6.png` (temporary signed query parameters intentionally not retained).
- Installed path: `preview.png`.
- Format/dimensions: PNG, 3840 × 2160; 4,288,628 bytes.
- Downloaded/installed SHA-256: `d221011258f3da5d9811388015a3750d2705fb5252b907b76185871d7307bf27`.

The pinned Git commit identifies the README reference; the image itself is **not a repository blob** and is pinned by the downloaded content hash. The actual decoded PNG was inspected and copied byte-for-byte. It depicts an Omarchy desktop, not Winarchy.

## Wallpaper

- Source: `backgrounds/1-synthwave-84.jpg` at the pinned revision.
- URL: https://raw.githubusercontent.com/omacom/omarchy-synthwave84-theme/283dbcf17c3a500b7d3ddfce081e1dc2b3641172/backgrounds/1-synthwave-84.jpg
- Installed path: `wallpapers/1-synthwave-84.jpg`.
- Format/dimensions: JPEG, 5314 × 2990; 7,232,828 bytes.
- Source/installed SHA-256: `f428d61b03d3f1c2b70342432d53e187c4ea5926cd4772d42f7f83240f62024d`.

The repository contains one wallpaper; it is preserved unchanged. No resizing, cropping, re-encoding, metadata changes or synthesized assets were applied. Pillow 11.1.0 was used only for decoding, dimensions and visual inspection, not rewriting delivered images.

## Palette and review input SHA-256

All paths below are repository files at the pinned revision:

- `README.md`: `08c7746ea4bb97ae0881a80ccd8183fcc9d5ea4a356b44fb61099f09a79c7d60`
- `alacritty.toml`: `40f5b1528c5c18f54b0653d69035f1c4b5c62600410a8a499f0214910525d2ce`
- `waybar.css`: `869bc81f30995d05a93d76bef70aabd9634d724d70b83a28fc11c71ce3b09faf`
- `walker.css`: `28222414fb2599bb43bb6707bbd5d16c53a974934d60a802568bf22bf61a0d01`
- `hyprland.conf`: `5fa8be33bc373251712fb7a40b1c382d0ea9f9fd0bc1f2042ee04fa8b53d85a7`
- `hyprlock.conf`: `e26323de531fb0ac4199b15ef7dd54898bf074c2316a8689dda4127a233dbd5b`
- `mako.ini`: `d588344702a7c7dd53fb0a931c58a5a35c0e2bd8e61451488fb2f9d05cffeb73`
- `swayosd.css`: `a5baad25ac7efdac39ec5c2fefc8dcba5434508cd3cd1cbd45f77665ab2c334c`
- `btop.theme`: `edf830839bd215cb033b7166fad3459f0d55b6ccc3dc8a1823ed12615d8220c4`

All 16 ANSI slots map exactly to Alacritty `[colors.normal]` and `[colors.bright]` in black/red/green/yellow/blue/magenta/cyan/white order. No generated terminal colors or Quattro template are needed.

The native palette was generated using the collection's `convert_palette.py` helper with:

```text
--name "Synthwave '84" --mode dark --ansi-source alacritty
--surface '#0d0221' --overlay '#614d85' --subtext '#ff7edb' --accent '#ff00ff'
```

The resulting comment was changed from draft to reviewed attribution; palette data was not otherwise modified. UI mapping and differences from the original application-specific styles are documented in README.md.

Generated `theme.toml` SHA-256: `bed0b31072c648a5d748f4a05bb5e3daf1ee0f6e32680261967d3c8cc5a32019`.
