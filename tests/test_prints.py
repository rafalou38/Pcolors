from unittest import TestCase
from Pcolors import cget
from Pcolors.exceptions import BadColorError, BadFormatError


class Test(TestCase):
	def test_cprint(self):
		self.assertEqual(
			cget(
				"test 123", "red"
			),
			"[31;49mtest 123[0m\n"
		)
		self.assertEqual(
			cget(
				"test 123", "lred"
			),
			"[91;49mtest 123[0m\n"
		)
		self.assertEqual(
			cget(
				"test 123",
				"red", "blue",
			), "[31;44mtest 123[0m\n"
		)
		self.assertEqual(
			cget(
				"test 123",
				"red", "lblue",
			), "[31;104mtest 123[0m\n"
		)
		self.assertEqual(
			cget(
				"test 123",
				"red", "lblue", end=""
			), "[31;104mtest 123[0m"
		)
		self.assertEqual(
			cget(
				"test 123",
				format=("bold",)
			), "[39;49;1mtest 123[0m\n"
		)
		self.assertEqual(
			cget(
				"test 123",
				format=("bold", "underline", "crossed")
			), "[39;49;1;4;9mtest 123[0m\n"
		)
		with self.assertRaises(BadFormatError):
			cget(
				"test 123",
				format=("bolds", "underline", "crossed")
			)
		with self.assertRaises(BadColorError):
			cget(
				"test 123",
				"reds"
			)

	def test_cprint_rgb(self):
		from Pcolors import cget
		from Pcolors.exceptions import BadColorError, BadFormatError
		self.assertEqual(
			cget(
				"test 123", "red"
			),
			"[31;49mtest 123[0m\n"
		)
		self.assertEqual(
			cget(
				"test 123", "lred"
			),
			"[91;49mtest 123[0m\n"
		)
		self.assertEqual(
			cget(
				"test 123",
				"red", "blue",
			), "[31;44mtest 123[0m\n"
		)
		self.assertEqual(
			cget(
				"test 123",
				"red", "lblue",
			), "[31;104mtest 123[0m\n"
		)
		self.assertEqual(
			cget(
				"test 123",
				"red", "lblue", end=""
			), "[31;104mtest 123[0m"
		)
		self.assertEqual(
			cget(
				"test 123",
				format=("bold",)
			), "[39;49;1mtest 123[0m\n"
		)
		self.assertEqual(
			cget(
				"test 123",
				format=("bold", "underline", "crossed")
			), "[39;49;1;4;9mtest 123[0m\n"
		)
		with self.assertRaises(BadFormatError):
			cget(
				"test 123",
				format=("bolds", "underline", "crossed")
			)
		with self.assertRaises(BadColorError):
			cget(
				"test 123",
				"reds"
			)
