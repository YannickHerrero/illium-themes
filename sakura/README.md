# Sakura (Winarchy personal adaptation)

Dark cherry-blossom theme adapted from [bjarneo/omarchy-sakura-theme](https://github.com/bjarneo/omarchy-sakura-theme): near-black plum background, warm off-white text, gold accent and a family of pink, coral and sand terminal tones.

## Palette

The upstream repository ships a Quattro `colors.toml` with `mode = "dark"`; there is no Alacritty configuration. The 16 ANSI slots follow Omarchy's official Alacritty template (pinned reference in `SOURCES.md`). The unconventional hues are preserved on purpose: the terminal `green` is salmon pink (`#f29b9a`), `blue` is the same gold as the accent (`#d9a56c`), and `cyan`/`magenta` are sand tones. No conventional green, blue or cyan has been introduced.

Winarchy UI mapping:

| Role | Color | Source / decision |
|---|---|---|
| Background | `#0d0509` | `background` |
| Bar surface | `#230e18` | `lighter_background` |
| Overlay / selection / unfocused border | `#853641` | upstream `brown`; see below |
| Text | `#f0eaed` | `foreground` |
| Secondary text | `#c6afba` | `dark_foreground` (9.8:1 on the base), rather than the fainter `muted` (3.4:1) |
| Accent | `#d9a56c` | `accent`; background text on it reaches 9.2:1 |
| Red / green / yellow | `#e85f6f` / `#f29b9a` / `#d4a882` | same named Quattro fields, unchanged |

The only explicit helper override is the overlay. Upstream `selection` (`#230e18`) is identical to `lighter_background`, so using it unchanged would make selections and unfocused borders indistinguishable from the bar (1.0:1). Upstream `brown` (`#853641`) comes from the same palette, separates from the base (2.5:1) and the bar (2.3:1), and keeps text readable on selections (6.8:1). `darker_background` (`#000000`) and `dark_background` (`#060204`) were rejected because they barely separate from the base (about 1.0:1).

Winarchy shares its accent between focused borders, active workspaces, launcher selection and the generic WezTerm cursor, and its overlay between selection and unfocused borders; these roles are not one-to-one with Omarchy's application-specific styles. This is a native Winarchy palette, not an installation of Omarchy configuration. The upstream `icons.theme` (`Yaru-red`) has no Winarchy equivalent and is ignored. No upstream code is executed.

## Preview and wallpapers

- `preview.png`: the upstream root `preview.png`, copied byte-for-byte (3841 x 2161). It is an Omarchy desktop screenshot supplied by the author, not a live rendering of Winarchy windows.
- `wallpapers/1.jpg` to `wallpapers/6.jpg`: the six upstream `backgrounds/` images, copied unchanged with their original numeric filenames (no resizing, recompression or metadata changes). They are all full-resolution desktop artwork: a pink moon over a snowy peak with blossoming trees, a cherry-blossom branch photograph, an orange sun over ink waves, a red tree on a misty lake, a watercolor temple by a pond, and an autumn forest with a lone warrior (apparently video-game fan art). No logos, badges or lock-screen assets exist upstream, so nothing is excluded.

See `SOURCES.md` for the exact revision, URLs, hashes and dimensions.

## Rights / distribution

No LICENSE file, explicit license grant or image-specific attribution was present in the upstream repository at the pinned revision (GitHub detects no license either). No permission to redistribute the theme, the screenshot or the underlying artwork is inferred from the repository owner or from the licenses of other Omarchy projects. Several wallpapers depict third-party characters or styles whose rights holders are not identified upstream. This pack is retained for the requested local personal setup only. Clarify rights with the author and the relevant artists before publishing or distributing it. No fabricated LICENSE file is included.

## Use

```powershell
winarchyctl theme install <path-to-this-folder>
winarchyctl theme set sakura
```

Or open **Alt+Shift+Space > Theme**, type `sakura` and press Enter. Wallpapers are available under **Wallpaper**, and **Ctrl+Alt+Shift+W** cycles them. Installation alone does not activate the theme or modify saved wallpaper choices.
