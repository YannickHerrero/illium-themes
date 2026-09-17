# Palette mapping and review

Winarchy requires `name`, nine six-digit RGB color strings and optionally `mode`, `ansi`, `brights`, `background_opacity`. Do not add provenance or wallpaper fields to `theme.toml`: the Rust parser rejects unknown fields. Use README/SOURCES and the conventional wallpaper folder instead.

## Shared opacity

Use `background_opacity = 0.85` for the standard Winarchy default (finite range
`0.0..1.0`). The helper emits it explicitly; it does not infer opacity from an
Omarchy application config. It affects the terminal, Files/Tasks backgrounds and
browser home, never web pages. Upgrade all Winarchy binaries before installing
this field. The legacy `terminal_background_opacity` alias is still accepted by
Winarchy; never emit both names.

## UI roles

| Winarchy | Quattro starting point | Review |
|---|---|---|
| `background` | `background` | Terminal, launcher and solid desktop base |
| `surface` | `lighter_background` | Bar; sometimes `dark_background` is more appropriate |
| `overlay` | `selection` | Shared selection background and unfocused border; needs separation from base/surface |
| `text` | `foreground` | Normal text on background and surface |
| `subtext` | `dark_foreground`, then `muted` | Secondary text must remain readable, not merely faint |
| `accent` | `accent` | Focused border, active workspace and launcher selection; background text must contrast against it |
| `red`, `green`, `yellow` | Same named source fields | Preserve artistic intent, even nonstandard/monochrome hues |

When only Alacritty is present: primary background/foreground, normal black as a draft surface, selection background as overlay, bright black as secondary text and normal blue as draft accent. Review accompanying shell styles instead of assuming these defaults are definitive. Supply explicit overrides where needed. Missing required colors fail rather than being invented.

Snow example: use source `lighter_background` (`#f7f7f7`) for the bar, `darker_background` (`#e6e6e6`) for overlay, and `dark_foreground` (`#565656`) for secondary text. Its original selection equals the bar surface, so using it unchanged would not distinguish those elements well. Keep the `#0a0a0a` accent and all named ANSI hues grayscale.

## Terminal arrays

Order for both arrays: **black, red, green, yellow, blue, magenta, cyan, white**.

If `alacritty.toml` supplies `[colors.normal]` and `[colors.bright]`, preserve those values in this order. The helper normalizes `0xRRGGBB`/`#RRGGBB` to lowercase `#rrggbb` without changing the color.

If the source has only Quattro `colors.toml`, use the mapping in Omarchy's `default/themed/alacritty.toml.tpl`:

```text
ansi    = background, red, green, yellow, blue, magenta, cyan, foreground
brights = muted, bright_red, bright_green, bright_yellow,
          bright_blue, bright_magenta, bright_cyan, bright_foreground
```

Reference verified at Omarchy revision `b679363bed05415771a1b1dc92c6899a908236f7`:
https://github.com/omacom/omarchy/blob/b679363bed05415771a1b1dc92c6899a908236f7/default/themed/alacritty.toml.tpl

Record that mapping provenance for Quattro-only adaptations. If the upstream format evolves, inspect its current pinned template before changing this rule.

## Visual checks

Check text on base and bar, selected text, active workspace/launcher selection, and inactive icons/text. Prefer adjustments drawn from the same source palette and explain them. A monochrome source must not acquire colored accents simply because ANSI roles are called red or green.

Do not automatically propagate a special cursor/search/selection color into every Winarchy role: the schemas are not one-to-one. Winarchy's generic WezTerm integration maps its accent to the cursor and overlay to selection; disclose material differences from upstream rather than claiming every application color is identical.
