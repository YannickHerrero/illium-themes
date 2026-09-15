# Previews and wallpaper assets

Read the target Winarchy `docs/themes.md` and current pack installer before
importing: formats and limits may evolve. The palette helper deliberately only
handles TOML; it does not download, copy, convert, install or activate images.

## Find a real preview

Use the same pinned revision as the palette when possible:

1. Look for a root `preview.png`, `preview.jpg` or `preview.jpeg` (case-insensitive).
2. Inspect alternate names such as `screenshot.png`, and images referenced by the
   pinned README. Only use an image that actually presents the desktop theme.
3. README previews may be GitHub user-attachment URLs, not files in the repository.
   Download the exact referenced URL with bounded reads. Record the README's
   commit/hash, original URL, final redirect origin/path if different, downloaded
   SHA-256, format and dimensions. Do not persist temporary signed authorization
   query strings from CDN redirects. The content hash pins the attachment, **not** the Git
   commit. Never claim a remote attachment has a repository path that it lacks.
4. Download to temporary staging and decode/inspect the file; an extension or an
   HTTP Content-Type alone does not establish that it is an image. Reject HTML,
   Git LFS pointers, malformed/oversized files and symlinks/reparse points.
5. Preserve supported original bytes. Rename an upstream `screenshot.png` to
   `preview.png`, for example, and explicitly document the mapping. Store the
   preview at the pack root, not inside `wallpapers/`.

Exclude `preview-unlock.*`, lock-screen images, badges, standalone logos and
screenshots of unrelated applications. If the author's `preview.png` only shows
artwork (Akane, for example), retain it but describe it as artwork, not a desktop
screenshot. Do not generate an imitation UI or switch the live desktop just to
create an absent screenshot.

## Picker behavior to account for

Winarchy recognizes static root `preview.png`, `preview.jpg`, `preview.jpeg`, in
that priority. Avoid redundant variants unless there is a deliberate reason:
installing a JPEG does not supersede an existing PNG. No TOML preview field is
supported. Filenames are case-insensitive; a converted WebP should become PNG,
not a WebP stream renamed to `.png`.

Without a dedicated preview, the picker uses the first alphabetically sorted
wallpaper, not the saved wallpaper choice. Without any usable image a theme has
no card. State this explicitly when no preview exists. Browsing never applies a
theme; confirmation does. Upstream screenshots depict **Omarchy**, not a live
preview of the user's Winarchy windows or applications.

The menu is **Alt+Shift+Space → Theme**; type to filter, browse with Left/Right
or Tab/Shift+Tab, then Enter to apply. `winarchyctl theme picker` opens the same
UI. The default Ctrl+Alt+Shift+Space shortcut may be absent from older user
keybinding files; do not silently rewrite those files during an import.

## Wallpapers and unsupported formats

Copy only real desktop backgrounds into the flat `wallpapers/` directory. A
full-resolution branded background remains a wallpaper; a small standalone logo
is not one. Preserve all supported original bytes and descriptive filenames.

When the upstream image format is unsupported (e.g. WebP):

- Use a local decoder, such as Pillow, to convert to PNG without resizing or
  cropping. Do not add a Winarchy runtime dependency merely to import one pack.
- Verify output dimensions and decoded RGBA pixel equality with the source.
  Conversion cannot recover losses already present in a lossy WebP/JPEG.
- Record source/output paths and SHA-256 hashes, converter/version, and any
  metadata/color-profile handling. Never label converted files byte-identical.
- Do not silently flatten animations/videos into a supposedly equivalent preview;
  prefer a supplied still, or document/agree a representative-frame extraction.
- Resolve duplicate basenames explicitly, including collisions after conversion.
- Check 32 MiB, 64 megapixels and 16384 maximum dimension per image, 64 wallpapers
  per pack, and the 512 MiB combined preview+wallpaper byte budget. Do not resize
  to bypass a limit without user agreement.

## Rights and provenance

Keep actual upstream licenses and image credits. A repository MIT license is not
a new license for every depicted photograph, character, logo or application.
External attachments may have different or unspecified terms. No explicit grant
means unclarified redistribution: keep the requested adaptation local and state
that reservation; do not invent a license or publish the images.

`SOURCES.md` should identify every asset's repository path or actual external
URL, full source revision where applicable, destination filename, dimensions,
source SHA-256, and output SHA-256 when transformed. Include the palette, shell
style and license inputs used in the conversion. Exclusions and material mapping
choices belong in README/SOURCES as well.

## Install and verify, without activation

Use the upgraded native `winarchyctl theme install` for new packs. Verify that
`themes/<id>/preview.*` actually exists afterward and matches the reviewed image;
also compare palettes, wallpapers and copied provenance. The directory watcher
notices image additions, including inactive themes, without a restart.

Existing packs are never overwritten by the installer. To add a missing preview
later, use exclusive/create-new file creation in the source and installed asset
folders. Preserve any existing preview variants, palette, wallpapers and docs.
If installed SOURCES.md has user changes, add `PREVIEW-SOURCES.md` rather than
replacing it. Capture and compare `winarchy.toml` and `wallpapers.json` before and
after. Adding an asset does not authorize selecting a theme, changing its saved
wallpaper, restarting the daemon, or rewriting keyboard shortcuts.
