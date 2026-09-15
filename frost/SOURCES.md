# Sources, Frost

Upstream: https://github.com/bjarneo/omarchy-frost-theme

Default branch inspected: `main`.
Pinned revision: `f702a288630c2c740101e6c677ed4c325a598df2` (commit "Adopt Omarchy Quattro theme format", 2026-08-30).

Repository tree at this revision: `.gitignore`, `README.md`, `colors.toml`, `icons.theme`, `preview.png`, `backgrounds/1.jpg`, `backgrounds/2.png`, `backgrounds/3.jpg`. All entries are regular blobs (mode 100644); no symlinks, submodules or LFS pointers. No LICENSE, `alacritty.toml` or light-mode marker is present. No upstream scripts were executed. This is a local personal adaptation, not a redistribution license (see README.md).

## Picker preview

- Source: `preview.png` at the pinned revision.
- URL: https://raw.githubusercontent.com/bjarneo/omarchy-frost-theme/f702a288630c2c740101e6c677ed4c325a598df2/preview.png
- Installed path: `preview.png`.
- Format/dimensions: PNG (RGBA), 3841 x 2161; 3,497,509 bytes.
- Source/installed SHA-256: `89df2cc9636ee86a94b41af1ea9f112bc255480a5626803574961e1286c1d9cd`.

Copied byte-for-byte. It is the image referenced by the pinned README and depicts an Omarchy desktop, not Winarchy.

## Wallpapers

All from `backgrounds/` at the pinned revision, base URL `https://raw.githubusercontent.com/bjarneo/omarchy-frost-theme/f702a288630c2c740101e6c677ed4c325a598df2/backgrounds/`. Filenames are preserved.

| Source path | Installed path | Format / dimensions | Bytes | SHA-256 (source = installed) |
|---|---|---|---:|---|
| `backgrounds/1.jpg` | `wallpapers/1.jpg` | JPEG, 4032 x 2622 | 2,462,535 | `5aff974665a0b5798f1f58ddb31daa47d498c0cbae4408c09bed1e84da63bfaf` |
| `backgrounds/2.png` | `wallpapers/2.png` | PNG (RGBA), 4000 x 2000 | 286,458 | `d9236a0f36167dc397b2201bd92d085925cf73a70911701fb6702d6ab631551e` |
| `backgrounds/3.jpg` | `wallpapers/3.jpg` | JPEG, 6144 x 3160 | 389,182 | `122fe1492adfb0e36c9950291328608fd00e2637d86791c80ddf9d0e67687080` |

`1.jpg` carries an EXIF ImageDescription that reads as an image-generator prompt (pixel-art snow-capped mountains, `--ar 3:2 --stylize 750`); its EXIF height field (2688) differs from the actual 2622 px, suggesting an upstream crop. The file is kept unchanged. No resizing, cropping, re-encoding, metadata changes or synthesized assets were applied. Pillow 11.1.0 was used only for decoding, dimensions and visual inspection.

## Palette and review input SHA-256

Repository files at the pinned revision:

- `colors.toml`: `4fdaf055ce4cc6f1d980209ccfdb0035c6ad16a418a02767242a4e331f96ccf8`
- `README.md`: `738f39886dead038979d8320ce19d8c566c5f2ca61565d29ff8574af4a21cb91`
- `icons.theme`: `75be55b00f24a3cfc708db729e9bca23765e8ef0991d6889fbb2fd4d29581209`
- `.gitignore`: `69aa73cf5bc3377a7d97f2e8d2bb773195815efe225af7f1be6f5b9306bbe14f`

## Terminal mapping

The source is Quattro-only and supplies no `alacritty.toml`. The 16 ANSI slots follow Omarchy's template at:
https://github.com/omacom/omarchy/blob/b679363bed05415771a1b1dc92c6899a908236f7/default/themed/alacritty.toml.tpl

Normal black/white map to `background`/`foreground`; bright black/white to `muted`/`bright_foreground`; the six named hues use their corresponding normal/bright fields. Exact correspondence between `theme.toml` and `colors.toml` was verified with a TOML parser.

## Generation

The native palette was generated with the collection's `convert_palette.py` helper using:

```text
--name "Frost" --overlay '#4e5b6b'
```

Mode came from upstream `mode = "dark"`. The overlay override uses upstream `brown`; the rationale is in README.md. The generated first-line comment was changed from draft to reviewed attribution; palette data was not otherwise modified.

Generated `theme.toml` SHA-256: `003744d0bd85366c9ef13bbdf9666ed76f0c0df55e0eace5f9355785c510f0b0`.
