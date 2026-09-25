import importlib.util
import subprocess
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "convert_palette.py"
spec = importlib.util.spec_from_file_location("convert_palette", SCRIPT)
converter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(converter)

COLORS = '''mode = "light"
background = "#ffffff"
foreground = "#0a0a0a"
bright_foreground = "#000000"
lighter_background = "#f7f7f7"
selection = "#f7f7f7"
muted = "#919191"
dark_foreground = "#565656"
accent = "#0a0a0a"
'''
COLORS += "".join(f'{k} = "#0a0a0a"\nbright_{k} = "#0a0a0a"\n' for k in converter.ORDER[1:7])


class ConversionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name)
        (self.source / "colors.toml").write_text(COLORS)

    def test_monochrome_quattro_and_explicit_overlay(self):
        p = converter.convert(self.source, "Snow", overlay="#e6e6e6")
        self.assertEqual(p["mode"], "light")
        self.assertEqual(p["background_opacity"], 0.85)
        self.assertNotIn("terminal_background_opacity", p)
        self.assertEqual(p["overlay"], "#e6e6e6")
        self.assertEqual(p["subtext"], "#565656")
        self.assertEqual(p["ansi"], ["#ffffff"] + ["#0a0a0a"] * 7)
        self.assertEqual(p["brights"], ["#919191"] + ["#0a0a0a"] * 6 + ["#000000"])
        for field in ("red", "green", "yellow", "accent"):
            self.assertEqual(p[field], "#0a0a0a")
        self.assertEqual(tomllib.loads(converter.render(p)), p)

    def test_legacy_arrays_take_precedence_unless_overridden(self):
        text = '[colors.primary]\nbackground = "#111111"\nforeground = "#eeeeee"\n'
        text += '[colors.selection]\nbackground = "#333333"\n'
        for section in ("normal", "bright"):
            text += f'[colors.{section}]\n'
            text += "".join(f'{k} = "0x{i:06X}"\n' for i, k in enumerate(converter.ORDER))
        (self.source / "alacritty.toml").write_text(text)
        p = converter.convert(self.source, "Legacy")
        self.assertEqual(p["ansi"], [f"#{i:06x}" for i in range(8)])
        self.assertEqual(converter.convert(self.source, "Quattro", ansi_source="colors")["ansi"][0], "#ffffff")
        (self.source / "colors.toml").unlink()
        with self.assertRaises(ValueError):
            converter.convert(self.source, "Legacy")
        self.assertEqual(converter.convert(self.source, "Legacy", mode="dark")["mode"], "dark")

    def test_missing_colors_do_not_get_invented(self):
        (self.source / "colors.toml").write_text(COLORS.replace('bright_red = "#0a0a0a"\n', ''))
        with self.assertRaisesRegex(ValueError, "bright_red"):
            converter.convert(self.source, "Incomplete")

    def test_invalid_rgb_mode_and_name(self):
        for kwargs in ({"accent": "#fff"}, {"mode": "unknown"}):
            with self.assertRaises(ValueError):
                converter.convert(self.source, "Snow", **kwargs)
        with self.assertRaises(ValueError):
            converter.convert(self.source, "Snow\nInjected")
        p = converter.convert(self.source, 'Snow "gris" é')
        self.assertEqual(tomllib.loads(converter.render(p))["name"], 'Snow "gris" é')

    def test_bounded_input_and_bad_toml(self):
        for content in (" " * 65537, "not valid toml"):
            (self.source / "colors.toml").write_text(content)
            with self.assertRaises(ValueError):
                converter.convert(self.source, "Snow")

    def test_symlink_input_is_rejected(self):
        path = self.source / "colors.toml"
        path.rename(self.source / "real.toml")
        try:
            path.symlink_to(self.source / "real.toml")
        except OSError:
            self.skipTest("symlinks unavailable")
        with self.assertRaises(ValueError):
            converter.convert(self.source, "Snow")

    def test_cli_refuses_overwrite(self):
        output = self.source / "theme.toml"
        command = [sys.executable, "-B", str(SCRIPT), str(self.source), "--name", "Snow", "--output", str(output)]
        subprocess.run(command, check=True, capture_output=True)
        original = output.read_bytes()
        result = subprocess.run(command, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(output.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
