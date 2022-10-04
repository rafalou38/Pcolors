from unittest import TestCase

from Pcolors.exceptions import BadFormatError, BadColorError
from Pcolors.style import style


class TestStyle(TestCase):
	def test_get_code(self):
		self.assertEqual(
			style(
				"red"
			).get_code(),
			"[31;49m"
		)
		self.assertEqual(
			style(
				"red", "blue"
			).get_code(),
			"[31;44m"
		)
		self.assertEqual(
			style(
				"lred", "blue"
			).get_code(),
			"[91;44m"
		)
		self.assertEqual(
			style(
				"lred", "lblue"
			).get_code(),
			"[91;104m"
		)
		self.assertEqual(
			style(
				"lred", "lblue",
				format=("bold",)
			).get_code(),
			"[91;104;1m"
		)
		self.assertEqual(
			style(
				"lred", "lblue",
				format=("bold", "rapid_blink")
			).get_code(),
			"[91;104;1;6m"
		)
		with self.assertRaises(BadFormatError):
			style(
				format=("bolds", "underline", "crossed")
			)

		with self.assertRaises(BadColorError):
			style(
				"reds"
			)

	def test_get_code_rgb(self):
		from Pcolors.style import style
		self.assertEqual(
			style(
				rgb_fg=[235, 64, 52]
			).get_code(),
			"[39;49;38;2;235;64;52m"
		)
		self.assertEqual(
			style(
				rgb_bg=[50, 168, 82]
			).get_code(),
			"[39;49;48;2;50;168;82m"
		)
		self.assertEqual(
			style(
				rgb_bg=[50, 168, 82],
				rgb_fg=[235, 64, 52]
			).get_code(),
			"[39;49;48;2;50;168;82;38;2;235;64;52m"
		)
		with self.assertRaises(BadColorError):
			style(
				rgb_bg=[50, 168],
				rgb_fg=[235, 64, 52]
			)
		with self.assertRaises(BadColorError):
			style(
				rgb_bg=[50, 168, 52],
				rgb_fg=[235, 64]
			)
		with self.assertRaises(BadColorError):
			style(
				rgb_bg=[50, 168, 52],
				rgb_fg=[235, 64]
			)

	def test_get_code_hex(self):
		self.assertEqual(
			style(
				rgb_fg="#eb4034"
			).get_code(),
			"[39;49;38;2;235;64;52m"
		)
		self.assertEqual(
			style(
				rgb_bg="#32a852",
			).get_code(),
			"[39;49;48;2;50;168;82m"
		)
		self.assertEqual(
			style(
				rgb_bg="#32a852",
				rgb_fg="#4287f5"
			).get_code(),
			"[39;49;48;2;50;168;82;38;2;66;135;245m"
		)
		with self.assertRaises(BadColorError):
			style(
				rgb_fg="#eb403"
			)
		with self.assertRaises(BadColorError):
			style(
				rgb_bg="#eb403x"
			)
		with self.assertRaises(BadColorError):
			style(
				rgb_fg="eb403x#"
			)
		with self.assertRaises(BadColorError):
			style(
				rgb_bg="#fff"
			)
		with self.assertRaises(BadColorError):
			style(
				rgb_fg=""
			)
