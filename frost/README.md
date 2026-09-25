# Frost, Illium (personal adaptation)

Cool, muted dark theme adapted from [bjarneo/omarchy-frost-theme](https://github.com/bjarneo/omarchy-frost-theme): a navy base with desaturated ice-blue and gray-blue tones, described upstream as inspired by frost patterns on a winter morning.

## Palette

The pinned upstream revision is Quattro-only: it supplies `colors.toml` with `mode = "dark"` and no `alacritty.toml`. Dark mode is taken from that explicit marker.

Illium UI mapping:

| Role | Color | Source / decision |
|---|---|---|
| Background | `#0a0f1c` | `background` |
| Bar surface | `#121b33` | `lighter_background` |
| Overlay / selection / unfocused border | `#4e5b6b` | `brown`, instead of `selection` (see below) |
| Text | `#d4d5d9` | `foreground` |
| Secondary text | `#9ea0a9` | `dark_foreground` |
| Accent | `#9bb0c2` | `accent` (also upstream `blue`) |
| Red / green / yellow | `#869aac` / `#95a8b8` / `#9fadb8` | Same named fields, unchanged |

The only explicit helper override is the overlay. Upstream `selection` (`#121b33`) is identical to `lighter_background`, so the shared Illium overlay role would have matched the bar exactly (1.00:1) and sat at 1.12:1 against the desktop base: unfocused window borders and launcher selections would have been nearly invisible. Upstream `brown` (`#4e5b6b`) is a mid-tone blue-gray from the same palette; it reaches 2.76:1 against the base, 2.47:1 against the bar, and keeps normal text at 4.72:1 on selected rows. Terminal selection therefore differs from upstream Alacritty/Neovim selection, which uses the `#121b33` tone; this is a deliberate Illium-only deviation.

Other review figures: text on base 13.04:1, text on bar 11.64:1, secondary text on base 7.34:1 and on bar 6.55:1, base-colored text on the accent 8.55:1. The bar surface is only 1.12:1 above the base; this faint separation is upstream intent and is kept.

The six named ANSI hues are intentionally desaturated blue-grays, not conventional red, green or yellow, and the bright variants equal the normal ones upstream. They are preserved exactly; no conventional hues were substituted. The 16 ANSI slots follow Omarchy's official Alacritty template for Quattro themes (pinned reference in `SOURCES.md`): normal black/white are `background`/`foreground`, bright black/white are `muted`/`bright_foreground`.

Generated with the collection's `omarchy-to-illium` palette helper, then reviewed. Upstream `icons.theme` (Yaru-blue) has no Illium equivalent and is not reproduced. No upstream scripts or configuration were executed.

## Preview and wallpapers

- `preview.png`: the unchanged upstream root `preview.png`, 3841 x 2161, an Omarchy desktop screenshot (btop, Neovim, fastfetch and a terminal over the layered-mountains wallpaper). It depicts Omarchy, not live Illium windows.
- `wallpapers/1.jpg`: pixel-art snow-capped mountains with a valley settlement, 4032 x 2622. Its EXIF description contains an image-generator prompt ("snow-capped mountains drawn in the style of pixel art ... --ar 3:2 --stylize 750"), so this appears to be AI-generated artwork; the repository gives no separate credit or terms.
- `wallpapers/2.png`: layered misty mountain silhouettes with pine ridges, 4000 x 2000.
- `wallpapers/3.jpg`: full-resolution blue-gray gradient carrying the dothash mark, 6144 x 3160 (a branded wallpaper, not a standalone icon; kept like Snow's dothash wallpaper).

Upstream filenames are numeric and are kept as they are. All images are copied byte-for-byte, without resizing or recompression. No lock-screen assets or standalone logos exist at the pinned revision.

## Rights / distribution

No LICENSE file or explicit license statement was present in the upstream repository or README at the pinned revision (GitHub also reports no detected license). No permission to redistribute the theme, the screenshot or the artwork is inferred from the repository owner or from the licenses of other Omarchy projects. This pack is retained for the requested local personal setup; clarify rights with the author before publishing or distributing it. No fabricated LICENSE file is included.

See `SOURCES.md` for the exact upstream revision, URLs and SHA-256 hashes.

## Use

```powershell
illiumctl theme install <path-to-this-folder>
illiumctl theme set frost
```

Or open **Alt+Shift+Space, then Theme**, type `frost` and press Enter. Wallpapers are available under **Wallpaper**, and **Ctrl+Alt+Shift+W** cycles them. Installation alone does not activate the theme or modify saved wallpaper choices.
