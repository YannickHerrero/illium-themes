# Snow — Winarchy (personal adaptation)

Monochrome light theme adapted from [bjarneo/omarchy-snow-theme](https://github.com/bjarneo/omarchy-snow-theme).

## Palette

White background (`#ffffff`), nearly black text/accent (`#0a0a0a`), light gray bar (`#f7f7f7`) and readable secondary text (`#565656`). These are upstream `background`, `foreground`/`accent`, `lighter_background` and `dark_foreground`.

Winarchy's shared overlay/selection/border role uses upstream `darker_background` (`#e6e6e6`) instead of `selection` (`#f7f7f7`), which equals the bar surface. This is the only explicit helper override and gives selections and borders more distinction.

The source provides only Quattro `colors.toml`, not Alacritty configuration. Its 16 ANSI slots follow Omarchy's official Alacritty template (pinned reference in `SOURCES.md`). The six named ANSI hues and their bright variants deliberately remain `#0a0a0a`; no conventional red, green or yellow has been introduced. Black/white slots follow the light terminal mapping, not the literal color names.

Generated with the local `omarchy-to-winarchy` skill's palette helper, then reviewed. All Winarchy UI and ANSI colors are grayscale.

## Wallpapers

All three upstream wallpapers are retained unchanged:

- `1-christina-gottardi-unsplash.jpg` — snowy landscape with a solitary tree, 4506×3004. The filename credits Christina Gottardi / Unsplash; the repository does not give the original photo URL or image-specific terms.
- `2-snow.jpg` — minimal light background, 3840×2160.
- `3-dothash-light.jpg` — full-resolution light wallpaper with the dothash mark, 3840×2160 (not a standalone UI icon).

## Picker preview

`preview.png` is the unchanged upstream Omarchy screenshot, used by Winarchy's visual picker. It does not claim to render Winarchy applications. Its source hash is recorded in `SOURCES.md`; the same local-only rights reservation below applies.

## Rights / distribution

No LICENSE or explicit license statement was present in the upstream repository at the pinned revision. No permission to redistribute the theme or third-party photographs is inferred. This pack is retained for the requested local personal setup; clarify rights before publishing it. The MIT licenses of other packs do not apply here.

See `SOURCES.md` for the exact upstream revision and source hashes.

## Use

```powershell
winarchyctl theme install <path-to-this-folder>
winarchyctl theme set snow
```

Or open **Alt+Shift+Space → Theme**, type `snow` and press Enter. Wallpapers are available under **Wallpaper**, and **Ctrl+Alt+Shift+W** cycles them. Installation does not activate the theme automatically.
