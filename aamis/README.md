# Aamis (Winarchy)

Dark theme adapted from [vyrx-dev/omarchy-aamis-theme](https://github.com/vyrx-dev/omarchy-aamis-theme) by Amit (vyrx-dev): near-black canvas, creamy text, warm amber highlights and a single red accent. The upstream theme was generated with [Aether](https://github.com/bjarneo/aether).

## Palette

Upstream ships an Aether-style `colors.toml` (accent, cursor, foreground, background, selection and `color0..15`), not the newer Quattro semantic format, together with `alacritty.toml`, `ghostty.conf` and `kitty.conf`. All four files agree on the same 16 terminal colors, and the pack preserves the Alacritty `[colors.normal]` and `[colors.bright]` values exactly, including the intentional tan `green` (`#cea37f`, identical in normal and bright) and the cream `magenta` (`#ede4c8`). No conventional green or purple has been substituted. Dark mode is chosen explicitly after reviewing the `#0f0f0f` background and the README description; the repository has no `light.mode` marker.

Winarchy UI mapping:

| Role | Color | Source / decision |
|---|---|---|
| Background | `#0f0f0f` | `colors.toml` background, Alacritty primary, Waybar and Walker base |
| Bar surface | `#0f0f0f` | Upstream Waybar uses the same color as the base; nothing lighter exists in the palette |
| Overlay / selection | `#706a6a` | Bright black: Walker border, btop `selected_bg`, SwayOSD border and the Hyprland border gradient endpoint |
| Text | `#eadccc` | `colors.toml` foreground |
| Secondary text | `#cea37f` | Normal green / Wofi `gray1` selection and btop box outlines, instead of the faint bright black |
| Accent | `#e2be8a` | `colors.toml` accent, Walker selected text, Wofi window border, normal blue |
| Red / green / yellow | `#e25d6c` / `#cea37f` / `#f4bb54` | Alacritty normal roles, unchanged |

Deviations from upstream, and why:

- The upstream selection background (`#e2be8a`) equals the accent. Winarchy uses the overlay for both selections and unfocused window borders, so reusing the accent there would make focused and unfocused borders identical. Bright black is used instead, following the upstream btop selected row (`#706a6a` under `#eadccc`, 3.94:1) and the Walker border.
- Bright black as secondary text would only reach 3.61:1 against the base and would coincide with the overlay. The tan `#cea37f` reaches 8.37:1 and keeps the warm amber character of the theme.
- Dark background text on the accent has 10.92:1 contrast.
- The upstream Hyprland active border is a near-black to gray gradient (`#0f0f0f` to `#706a6a`); Winarchy uses the single amber accent for the focused border, active workspace and launcher selection, matching Walker's selected text rather than the gradient.

Winarchy's generic WezTerm integration maps the accent to the cursor (upstream uses the cream foreground) and the overlay to the selection. Application-specific styles (btop, Neovim, Vicinae, Typora, Vesktop, VS Code) are not reproduced: this is a native Winarchy palette, not an installation of Omarchy configuration. No upstream file is executed.

## Preview and wallpaper

- `preview.png`: upstream `assets/homescreen.png`, copied byte-for-byte (1921 x 1081). It is the Omarchy desktop screenshot the upstream README captions "Omarchy homescreen setup", showing Waybar over the wallpaper. It depicts Omarchy, not Winarchy. The other README images (`setup.png`, `lazygit.png`, `btop.png`, `neovim.png`) are application screenshots and `pallete.png` is a swatch strip; they are not previews and are not included.
- `wallpapers/wallhaven-mdjrqy.jpg`: the single upstream wallpaper, 5120 x 2880, copied without resizing or recompression. The filename indicates a wallhaven.cc image (id `mdjrqy`) by a third-party artist.
- `assets/icons/*` are standalone logo files for the Vicinae theme and are excluded; they are not desktop artwork.

See `SOURCES.md` for the pinned revision, URLs, hashes and dimensions.

## Rights

The upstream repository is MIT licensed (`LICENSE`, Copyright (c) 2025 Amit); the license file is preserved. That license covers the theme files, but it does not establish rights to the wallpaper, which is a wallhaven-hosted illustration by an unidentified third-party artist, nor to any application branding visible in the screenshot. Clarify the wallpaper's terms before publishing or redistributing this pack beyond personal use. Credits from the upstream README: Vicinae theme and logo by @lukapmoran, Typora theme by @pymmog, VS Code theme by @fedesapuppo.

## Use

```powershell
winarchyctl theme install <path-to-this-folder>
winarchyctl theme set aamis
```

Or open **Alt+Shift+Space > Theme**, type `aamis` and press Enter. The wallpaper is available under **Wallpaper**. Installation alone does not activate the theme or modify saved wallpaper choices.
