# Akane — Winarchy (personal adaptation)

Dark theme adapted from [Grenish/omarchy-akane-theme](https://github.com/Grenish/omarchy-akane-theme): dusk navy, parchment text, vermillion accent, moss and sunset gold.

The palette comes from upstream `colors.toml`. Winarchy's surface uses `lighter_background`, overlay uses `selection`, and secondary text uses `dark_foreground` rather than the darker `muted`. All 16 Alacritty colors are preserved exactly.

Includes the eight numbered upstream wallpapers, unchanged. The small `backgrounds/omarchy.png` logo is intentionally excluded because it is not desktop artwork. See `SOURCES.md` for the pinned revision and hashes.

## Picker preview

`preview.png` preserves the upstream author's preview artwork unchanged. The visual picker uses it instead of a wallpaper fallback. This upstream image shows the scenery only, not a composite of Winarchy windows. No preview-unlock/lock-screen assets are included. See `SOURCES.md` for its hash.

## Rights / distribution

No explicit license was present in the upstream repository at the pinned revision. No license or permission to redistribute its artwork is inferred or granted by this adaptation. These files are retained locally for the requested personal setup. Clarify permission with the upstream author before publishing this pack or its images; do not treat the licenses of the neighboring packs as applying here.

Install: `winarchyctl theme install <path-to-this-folder>`, then `winarchyctl theme set akane`.
