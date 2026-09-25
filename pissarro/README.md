# Pissarro — Illium

Light theme adapted from [mattbbia/pissarro](https://github.com/mattbbia/pissarro).

The warm cream background, olive text and lavender accent come from `colors.toml`. Illium's surface uses `lighter_background`, its overlay uses `dark_background`, and secondary text uses `bright_foreground` for better readability than `muted` on the light bar. The olive selection color is not used as an overlay because Illium shares that role between selection backgrounds and borders. The original 16 Alacritty colors are preserved exactly, including the artistic interpretation of red/green/magenta.

Includes all five upstream wallpapers, without resizing or recompression:

- Charing Cross Bridge London (1890)
- Hampton Court Green (1891)
- Landscape Ile De France (1873)
- Place Du Carrousel Paris (1900)
- The Louvre Afternoon Rainy Weather (1900)

The visual picker uses the upstream `preview.png` unchanged. It depicts Omarchy rather than Illium; its exact revision and hash are recorded in `SOURCES.md`.

The upstream project states that these Camille Pissarro paintings are public domain and that its source images came from the National Gallery of Art. The upstream MIT license is preserved in `LICENSE`; exact source revision and hashes are in `SOURCES.md`.

Install: `illiumctl theme install <path-to-this-folder>`, then `illiumctl theme set pissarro`.
