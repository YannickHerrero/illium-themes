# Sources: Sakura

Upstream: https://github.com/bjarneo/omarchy-sakura-theme

Default branch inspected: `main`.
Pinned revision: `dfeae9b8d245af05e16cf8bf3b89b743c94573d3` (commit "Adopt Omarchy Quattro theme format", 2026-08-30).

No LICENSE file, README license grant, `alacritty.toml` or `light.mode` marker is present at this revision; `colors.toml` declares `mode = "dark"`. All tree entries are regular `100644` blobs (no symlinks, submodules or LFS pointers). No upstream scripts or configuration were executed. This is a local personal adaptation, not a redistribution license (see README.md).

## Preview

- Source: `preview.png` at the pinned revision.
- URL: https://raw.githubusercontent.com/bjarneo/omarchy-sakura-theme/dfeae9b8d245af05e16cf8bf3b89b743c94573d3/preview.png
- Installed path: `preview.png`.
- Format/dimensions: PNG (RGBA), 3841 x 2161; 4,695,691 bytes.
- Source/installed SHA-256: `6a4649be447082c064d746bf886a4c102f8cd4e10ed149cb5336f8e09fc5bdef`.

Copied byte-for-byte. It depicts an Omarchy desktop (terminal, editor, file manager and system monitor), not Winarchy.

## Wallpapers

All six files come from `backgrounds/` at the pinned revision, URL prefix `https://raw.githubusercontent.com/bjarneo/omarchy-sakura-theme/dfeae9b8d245af05e16cf8bf3b89b743c94573d3/backgrounds/`. Destination filenames are identical to the source basenames.

| Source | Installed | Format/dimensions | Bytes | SHA-256 |
|---|---|---|---|---|
| `backgrounds/1.jpg` | `wallpapers/1.jpg` | JPEG, 8020 x 4495 | 12,515,061 | `098ac2f8751233e7d0525bed7c4036e05a19f4ebc244d063ea07f5827a128013` |
| `backgrounds/2.jpg` | `wallpapers/2.jpg` | JPEG, 6000 x 3375 | 4,278,009 | `79fa9b79d0c65c6aaab46d5e627cd3b283e7e817f319b3bbda498675fd0216a6` |
| `backgrounds/3.jpg` | `wallpapers/3.jpg` | JPEG, 3840 x 2160 | 1,325,560 | `0b2d21647340dc88ca6c113b3bd80bd41d288e17f01acf75fff87486345b4a34` |
| `backgrounds/4.jpg` | `wallpapers/4.jpg` | JPEG, 3840 x 2160 | 1,418,347 | `29491a2965b130b7ee2164dd70f6cbf0acb581ca4c038e5d4442707c135f3bf9` |
| `backgrounds/5.jpg` | `wallpapers/5.jpg` | JPEG, 3840 x 2160 | 1,172,921 | `697f10ccb08bd7081d1456c1662969e0edc8176be43b49ea0eee2b257b2f5e44` |
| `backgrounds/6.jpg` | `wallpapers/6.jpg` | JPEG, 6300 x 3600 | 4,100,128 | `d6ca6bf6eb1d2632a83cb738e02489dd916112a0e492d707e58edcfc12d2d4c2` |

All images are preserved unchanged (no resizing, cropping, re-encoding or metadata changes), so source and installed hashes are identical. Every image is within the installer limits (largest: 36.05 megapixels, 8020 px, 12.5 MB; about 29.5 MB in total). Pillow 11.1.0 was used only to decode, measure and visually inspect the images, never to rewrite delivered files. The repository contains no other images; nothing was excluded.

## Palette and review input SHA-256

Repository files at the pinned revision:

- `colors.toml`: `54fb3f6ae6757eb4b733b93b682004bb65fc701bc5e10dba137bfeabdffd6c42`
- `README.md`: `e1c14d1e2dacc1413fef28980f08fd600dd263a577492d6b5862f5ba3bdf7a4e`
- `icons.theme` (`Yaru-red`, not used): `1c2342215182a8e2880028e03e679fad194dbdfa5155b55daf8386390526cfbc`
- `.gitignore` (not used): `69aa73cf5bc3377a7d97f2e8d2bb773195815efe225af7f1be6f5b9306bbe14f`

The 16 ANSI slots are generated from Quattro `colors.toml` with Omarchy's official Alacritty template mapping (`ansi` = background, red, green, yellow, blue, magenta, cyan, foreground; `brights` = muted, bright_red, bright_green, bright_yellow, bright_blue, bright_magenta, bright_cyan, bright_foreground), verified at Omarchy revision `b679363bed05415771a1b1dc92c6899a908236f7`:
https://github.com/omacom/omarchy/blob/b679363bed05415771a1b1dc92c6899a908236f7/default/themed/alacritty.toml.tpl

No upstream Alacritty file exists; the terminal arrays are derived, not copied.

The native palette was generated with the collection's `skills/omarchy-to-winarchy/scripts/convert_palette.py` helper using:

```text
--name "Sakura" --overlay '#853641'
```

Mode was taken from upstream `colors.toml`. The header comment was changed from draft to reviewed attribution; palette data was not otherwise modified. The overlay override (upstream `brown` instead of `selection`, which equals the bar surface) is explained in README.md.

Generated `theme.toml` SHA-256: `9e7383e0ad9fcca055375eb469f417e2c25ea613925dd1cb776f0cc46351b44e`.
