# Sources: Futurism

Upstream: https://github.com/bjarneo/omarchy-futurism-theme

Default branch inspected: `main`.
Pinned revision: `e60be451d92565da43bd7976c488af3e983370bc` (commit "Adopt Omarchy Quattro theme format", 2026-08-30).

No LICENSE file or explicit README license grant is present at this revision; GitHub reports no detected license. No upstream scripts/configuration (`neovim.lua`) were executed. This is a local personal adaptation, not a redistribution license (see README.md).

All repository files below were downloaded from `https://raw.githubusercontent.com/bjarneo/omarchy-futurism-theme/e60be451d92565da43bd7976c488af3e983370bc/<path>`. Every blob in the pinned tree has regular mode `100644`; there are no symlinks, submodules or Git LFS pointers.

## Preview

- Source: `preview.png` (repository root) at the pinned revision.
- Installed path: `preview.png` (same name, same bytes).
- Format/dimensions: PNG, 2560 x 1440, RGBA (fully opaque); 2,372,859 bytes.
- Source/installed SHA-256: `8604fbbbe8981cb2ec4d88afecd7f1dbd63e3ebf07f99aafd366e8be57de3ed7`.

It is the same image referenced by the pinned README (`![Futurism preview](preview.png)`). It depicts an Omarchy desktop, not Winarchy.

## Wallpapers

All four files under upstream `backgrounds/` are installed under `wallpapers/` with the same basename and unchanged bytes. No resizing, cropping, re-encoding or metadata changes were applied; Pillow 11.1.0 was used only for decoding, dimensions and visual inspection.

| Source path | Installed path | Format / dimensions | Bytes | SHA-256 |
|---|---|---|---:|---|
| `backgrounds/1-futurism.jpg` | `wallpapers/1-futurism.jpg` | JPEG, 3840 x 2160 | 3,794,137 | `aefe40d4c63634c837c213170f778770bd009d49e8b13b913d46cbc443aa5782` |
| `backgrounds/2-futurism.png` | `wallpapers/2-futurism.png` | PNG, 3840 x 2160, RGB | 13,142,204 | `f48c4f4e5ccb5168abb2252d925687bf55cf2f6a43d6fe06775887c048315acd` |
| `backgrounds/3-futurism.png` | `wallpapers/3-futurism.png` | PNG, 3840 x 2160, RGBA (opaque) | 998,364 | `a8e0afa4931374048f08161bfa0b0c21771518b888290541f706a8bcccf85e64` |
| `backgrounds/4-futurism.jpg` | `wallpapers/4-futurism.jpg` | JPEG, 3840 x 2160 | 4,250,769 | `63c6fec5f0188919ea22b13688d77bf95661d59358f7ef8f09d10884306b790c` |

Files 1, 2 and 4 are third-party cyberpunk cityscape artworks without credits upstream; file 3 is a branded full-resolution wallpaper. Nothing was excluded.

## Palette and review input SHA-256

Repository files at the pinned revision:

- `README.md`: `772607a9558cf37e92f707ca48d5b80e7ecb39d9d6e8220dc2c39ec6059683a9`
- `colors.toml`: `45615167583b07a2a9195162fda729fcd8b25ebfbf69ad36e51f2bdd6162eb38`
- `icons.theme`: `328fd2519268a09cbcb45b3e8393f6abcc1739b9816bdc87bd4761d9d240f026` (not used)
- `neovim.lua`: `140fb185a529c23dcbcbe5ca6ed3ffe3f418decb16a80e81243207c4c4089172` (not used, not executed)

The upstream revision has no `alacritty.toml`. The `ansi` and `brights` arrays are generated from `colors.toml` with Omarchy's Quattro template mapping, verified at Omarchy revision `b679363bed05415771a1b1dc92c6899a908236f7`:
https://github.com/omacom/omarchy/blob/b679363bed05415771a1b1dc92c6899a908236f7/default/themed/alacritty.toml.tpl

```text
ansi    = background, red, green, yellow, blue, magenta, cyan, foreground
brights = muted, bright_red, bright_green, bright_yellow,
          bright_blue, bright_magenta, bright_cyan, bright_foreground
```

The native palette was generated with the collection's `convert_palette.py` helper:

```text
--name "Futurism" --surface '#080f1e'
```

`mode = "dark"` was taken from upstream `colors.toml`. The only override is the bar surface (`dark_background` instead of `lighter_background`, which upstream shares with `selection`); the rationale is in README.md. The generated header comment was changed from draft to reviewed attribution; palette data was not otherwise modified.

Generated `theme.toml` SHA-256: `cccb3dbe6c20acf1518aa4231700df61213a01b4d21086dceef5a3e2fa81676c`.
