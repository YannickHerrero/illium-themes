# Synthwave '84 — Winarchy (personal adaptation)

Dark neon theme adapted from [omacom/omarchy-synthwave84-theme](https://github.com/omacom/omarchy-synthwave84-theme): deep violet, magenta, electric blue/cyan and yellow.

## Palette

The upstream version supplies Alacritty and application-specific styles, not Quattro `colors.toml`. All 16 Alacritty ANSI colors are preserved exactly, including the intentional purple normal `green` (`#8f00ff`) and orange-red bright `green` (`#fe5442`). No conventional greens have been substituted. Dark mode is explicitly selected after reviewing the very dark background and shell surfaces; the repository has no light-mode marker.

Winarchy UI mapping:

| Role | Color | Source / decision |
|---|---|---|
| Background | `#240037` | Alacritty primary / Walker base |
| Bar surface | `#0d0221` | Waybar background |
| Text | `#ffffff` | Alacritty primary / Waybar foreground |
| Accent | `#ff00ff` | Walker selected text and Alacritty cursor |
| Overlay / selection | `#614d85` | Alacritty bright black; no upstream Alacritty selection background is defined |
| Secondary text | `#ff7edb` | Alacritty bright magenta, instead of faint bright-black text |
| Red / green / yellow | `#ff0040` / `#8f00ff` / `#f3e70f` | Alacritty normal roles, unchanged |

Winarchy shares its accent between focused borders, active workspaces, launcher selection and the generic WezTerm cursor. Magenta follows upstream Walker/cursor behavior; this deliberately differs from the original purple Hyprland border (`#8f00ff`). Dark text on that purple has about 3.20:1 contrast, versus 5.92:1 on magenta. Bright black is used for the selection surface rather than secondary text (only 2.57:1 against the base); the pink secondary text reaches 8.19:1 against the base, and white on the chosen overlay is 7.22:1. Every chosen color comes from the upstream palette or shell styles.

Application-specific notification colors, glow effects and mixed/gradient borders are not reproduced: this is a native Winarchy palette, not an installation of Omarchy configuration. Source files are never executed.

## Preview and wallpaper

- `preview.png`: the original 3840 × 2160 Omarchy screenshot linked in the pinned upstream README, downloaded from a GitHub user attachment and copied byte-for-byte. The attachment is pinned by its own SHA-256, not claimed to be a Git blob. It depicts Omarchy, not live Winarchy windows.
- `wallpapers/1-synthwave-84.jpg`: the single upstream wallpaper, 5314 × 2990, copied without resizing or recompression. No additional wallpapers or lock-screen assets are invented.

See `SOURCES.md` for the exact revision, URLs, source-file hashes and image dimensions.

## Rights / distribution

No LICENSE file, explicit license grant or image-specific attribution was present in the upstream repository/README at the pinned revision. No permission to redistribute the theme, the screenshot, or underlying third-party artwork/brands is inferred from the repository owner or the licenses of other Omarchy projects. This pack is retained for the requested local personal setup. Clarify rights with the authors and relevant image rights holders before publishing or distributing it. No fabricated LICENSE file is included.

## Use

```powershell
winarchyctl theme install <path-to-this-folder>
winarchyctl theme set synthwave84
```

Or open **Alt+Shift+Space → Theme**, type `synthwave84` and press Enter. The wallpaper is available under **Wallpaper**. Installation alone does not activate the theme or modify saved wallpaper choices.
