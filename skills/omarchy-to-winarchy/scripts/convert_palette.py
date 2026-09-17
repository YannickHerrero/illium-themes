#!/usr/bin/env python3
"""Generate a reviewed-later Winarchy palette from local Omarchy TOML. No network."""
import argparse
import json
import re
import stat
import sys
import tomllib
from pathlib import Path

ORDER = ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white")


def read_toml(path):
    meta = path.lstat()
    if not stat.S_ISREG(meta.st_mode) or getattr(meta, "st_file_attributes", 0) & 0x400:
        raise ValueError(f"{path}: expected regular non-reparse file")
    with path.open("rb") as stream:
        data = stream.read(65537)
    if len(data) > 65536:
        raise ValueError(f"{path}: exceeds 64 KiB")
    return tomllib.loads(data.decode("utf-8"))


def rgb(value, role):
    if not isinstance(value, str) or not re.fullmatch(r"(?:#|0x)[0-9a-fA-F]{6}", value):
        raise ValueError(f"{role}: missing/invalid six-digit RGB color: {value!r}")
    return "#" + value[-6:].lower()


def convert(source, name, mode=None, ansi_source="auto", **overrides):
    if not name or len(name) > 200 or any(ord(c) < 32 or ord(c) == 127 for c in name):
        raise ValueError("name must be a nonempty display name without control characters")
    colors_path, terminal_path = source / "colors.toml", source / "alacritty.toml"
    colors = read_toml(colors_path) if colors_path.exists() else {}
    terminal = read_toml(terminal_path).get("colors", {}) if terminal_path.exists() else {}
    if not colors and not terminal:
        raise ValueError("requires colors.toml or alacritty.toml; adapt other formats manually")
    mode = mode or colors.get("mode") or ("light" if (source / "light.mode").is_file() else None)
    if mode not in ("light", "dark"):
        raise ValueError("mode is not explicit upstream; pass --mode light or --mode dark after review")
    use_terminal = ansi_source == "alacritty" or (ansi_source == "auto" and bool(terminal))
    if use_terminal:
        normal, bright = terminal.get("normal", {}), terminal.get("bright", {})
        ansi = [rgb(normal.get(k), f"colors.normal.{k}") for k in ORDER]
        brights = [rgb(bright.get(k), f"colors.bright.{k}") for k in ORDER]
    else:
        # Omarchy Quattro default/themed/alacritty.toml.tpl mapping; do not guess black/white.
        ansi_keys = ("background", *ORDER[1:7], "foreground")
        bright_keys = ("muted", *("bright_" + k for k in ORDER[1:7]), "bright_foreground")
        ansi = [rgb(colors.get(k), k) for k in ansi_keys]
        brights = [rgb(colors.get(k), k) for k in bright_keys]
    primary = terminal.get("primary", {})
    # Winarchy's shared default, not an inferred Omarchy application setting.
    palette = {"name": name, "mode": mode, "background_opacity": 0.85}
    defaults = {
        "background": colors.get("background", primary.get("background")),
        "surface": colors.get("lighter_background", ansi[0]),
        "overlay": colors.get("selection", terminal.get("selection", {}).get("background")),
        "text": colors.get("foreground", primary.get("foreground")),
        "subtext": colors.get("dark_foreground", colors.get("muted", brights[0])),
        "accent": colors.get("accent", ansi[4]),
        "red": colors.get("red", ansi[1]),
        "green": colors.get("green", ansi[2]),
        "yellow": colors.get("yellow", ansi[3]),
    }
    for role, value in defaults.items():
        palette[role] = rgb(overrides.get(role) or value, role)
    palette.update(ansi=ansi, brights=brights)
    return palette


def render(palette):
    lines = ["# Winarchy adaptation draft; see README.md and SOURCES.md for reviewed mapping."]
    for key, value in palette.items():
        lines.append(f"{key} = {json.dumps(value, ensure_ascii=False)}")
    text = "\n".join(lines) + "\n"
    assert tomllib.loads(text) == palette
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="local folder of reviewed upstream files")
    parser.add_argument("--name", required=True, help="display name, not the pack folder identifier")
    parser.add_argument("--mode", choices=("light", "dark"))
    parser.add_argument("--ansi-source", choices=("auto", "alacritty", "colors"), default="auto")
    for role in ("background", "surface", "overlay", "text", "subtext", "accent"):
        parser.add_argument("--" + role, help="explicit reviewed RGB override")
    parser.add_argument("--output", type=Path, help="create a NEW file; otherwise print TOML")
    args = vars(parser.parse_args())
    output = args.pop("output")
    try:
        text = render(convert(**args))
        if output:
            with output.open("x", encoding="utf-8", newline="\n") as stream:
                stream.write(text)
        else:
            print(text, end="")
    except (OSError, ValueError, TypeError, AttributeError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
