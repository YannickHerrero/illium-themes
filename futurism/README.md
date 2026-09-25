# Futurism (Illium, personal adaptation)

Dark neon theme adapted from [bjarneo/omarchy-futurism-theme](https://github.com/bjarneo/omarchy-futurism-theme) by Bjarne Øverli: deep navy base, alice-blue text, hot pink accent and electric cyan.

## Palette

The upstream revision uses the Omarchy Quattro `colors.toml` format and declares `mode = "dark"` explicitly. There is no `alacritty.toml`, so both terminal arrays are derived with Omarchy's official `default/themed/alacritty.toml.tpl` mapping (see `SOURCES.md`). Every value comes from the upstream `colors.toml`; no color was invented.

The named terminal hues are deliberately unconventional and are preserved as-is: `red` and `magenta` are the pink accent (`#ff40a3`), `green` is electric cyan (`#00bfff`), `yellow` is a steel blue (`#5076b2`), and `blue`/`cyan` equal the foreground (`#f0f8ff`). No conventional red, green or yellow has been substituted.

Illium UI mapping:

| Role | Color | Source / decision |
|---|---|---|
| Background | `#0a1428` | `background` |
| Bar surface | `#080f1e` | `dark_background` (override, see below) |
| Overlay / selection | `#17294a` | `selection`, unchanged |
| Text | `#f0f8ff` | `foreground` |
| Secondary text | `#9dacbe` | `dark_foreground` |
| Accent | `#ff40a3` | `accent` |
| Red / green / yellow | `#ff40a3` / `#00bfff` / `#5076b2` | Same named fields, unchanged |

Single deviation from the helper defaults: upstream `selection` and `lighter_background` are the same color (`#17294a`), so using both as bar surface and overlay would make the bar, the selection background and the unfocused border indistinguishable. The bar therefore uses `dark_background` (`#080f1e`, slightly darker than the desktop base) and the upstream selection color is kept for the overlay. `darker_background` was not used because it is nearly invisible against the base.

Contrast review (WCAG ratios): text on base 17.1:1, text on the bar 18:1, secondary text on base 7.9:1, selected text on overlay 13.5:1, base-colored text on the pink accent 5.7:1. The overlay is subtle against the base (1.27:1), which matches the upstream selection intent. `muted` (`#53627a`, 2.97:1) is only used as bright black, not as secondary text.

Illium shares its accent between focused borders, active workspaces, launcher selection and the generic WezTerm cursor; upstream application-specific styles (Neovim Tokyo Night Storm, icon theme) are not reproduced. This is a native Illium palette, not an installation of Omarchy configuration. Source files are never executed.

## Preview and wallpapers

- `preview.png`: upstream root `preview.png`, 2560 x 1440 PNG, copied byte-for-byte. It is a screenshot of an Omarchy desktop (Neovim, btop, fastfetch, terminal), not live Illium windows.
- `wallpapers/1-futurism.jpg`, `2-futurism.png`, `4-futurism.jpg`: the three neon cyberpunk cityscape artworks from upstream `backgrounds/`, 3840 x 2160, copied without resizing or recompression.
- `wallpapers/3-futurism.png`: the full-resolution branded wallpaper (cyan drop logo over dark teal waves), 3840 x 2160, kept because it is a complete desktop background, not a standalone logo icon.

Nothing was excluded, converted or renamed except the location change into `wallpapers/`. See `SOURCES.md` for the exact revision, URLs, hashes and dimensions.

## Rights / distribution

The upstream repository has no LICENSE file and no license grant in its README at the pinned revision, and GitHub reports no detected license. The upstream README also carries no credits for the cityscape artworks, whose authors are unknown; the first wallpaper was evidently downloaded from Wallhaven (its original filename is visible in the upstream preview screenshot). No permission to redistribute the palette, the screenshot or the artwork is inferred. This pack is retained for the requested local personal setup only. Clarify rights with the theme author and the artwork rights holders before publishing or distributing it. No fabricated LICENSE file is included.

## Use

```powershell
illiumctl theme install <path-to-this-folder>
illiumctl theme set futurism
```

Or open **Alt+Shift+Space, Theme**, type `futurism` and press Enter. The wallpapers are available under **Wallpaper**. Installation alone does not activate the theme or modify saved wallpaper choices.
