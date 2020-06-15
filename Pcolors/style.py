from .exceptions import BadColorError, BadFormatError
from ._functions.code import code


class style():
	"""
	!this will not end the ANSI escape you will have to add \\033[0m or Pcolors.Code(Pcolors.shortcuts.format.normal)
	or use cprint
	"""

	def get_code(self):
		print(self.fg_code)
		print(self.bg_code)
		print(self.format)
		a = f"{code(self.fg_code, self.bg_code + 10, tuple(self.format))}"
		return a

	def __init__(self, fg_color=39, bg_color=49, end="\n", format=[], returnv=False):

		if fg_color == 30 or fg_color == "lblack":
			self.fg_code = 30
		elif fg_color == 31 or fg_color == "lred":
			self.fg_code = 31
		elif fg_color == 32 or fg_color == "lgreen":
			self.fg_code = 32
		elif fg_color == 33 or fg_color == "lyellow":
			self.fg_code = 33
		elif fg_color == 34 or fg_color == "lblue":
			self.fg_code = 34
		elif fg_color == 35 or fg_color == "lmagenta":
			self.fg_code = 35
		elif fg_color == 36 or fg_color == "lcyan":
			self.fg_code = 36
		elif fg_color == 37 or fg_color == "lwhite":
			self.fg_code = 37

		# dark colors
		elif fg_color == 90 or fg_color == "black":
			self.fg_code = 90
		elif fg_color == 91 or fg_color == "red":
			self.fg_code = 91
		elif fg_color == 92 or fg_color == "green":
			self.fg_code = 92
		elif fg_color == 93 or fg_color == "yellow":
			self.fg_code = 93
		elif fg_color == 94 or fg_color == "blue":
			self.fg_code = 94
		elif fg_color == 95 or fg_color == "magenta":
			self.fg_code = 95
		elif fg_color == 96 or fg_color == "cyan":
			self.fg_code = 96
		elif fg_color == 97 or fg_color == "white":
			self.fg_code = 97
		elif fg_color == 0 or fg_color == "normal":
			self.fg_code = 0
		elif fg_color == 39:
			self.fg_code = 39

		else:
			raise BadColorError(fg_color)

		if bg_color == 30 or bg_color == "lblack":
			self.bg_code = 30
		elif bg_color == 31 or bg_color == "lred":
			self.bg_code = 31
		elif bg_color == 32 or bg_color == "lgreen":
			self.bg_code = 32
		elif bg_color == 33 or bg_color == "lyellow":
			self.bg_code = 33
		elif bg_color == 34 or bg_color == "lblue":
			self.bg_code = 34
		elif bg_color == 35 or bg_color == "lmagenta":
			self.bg_code = 35
		elif bg_color == 36 or bg_color == "lcyan":
			self.bg_code = 36
		elif bg_color == 37 or bg_color == "lwhite":
			self.bg_code = 37

		# dark colors
		elif bg_color == 90 or bg_color == "black":
			self.bg_code = 90
		elif bg_color == 91 or bg_color == "red":
			self.bg_code = 91
		elif bg_color == 92 or bg_color == "green":
			self.bg_code = 92
		elif bg_color == 93 or bg_color == "yellow":
			self.bg_code = 93
		elif bg_color == 94 or bg_color == "blue":
			self.bg_code = 94
		elif bg_color == 95 or bg_color == "magenta":
			self.bg_code = 95
		elif bg_color == 96 or bg_color == "cyan":
			self.bg_code = 96
		elif bg_color == 97 or bg_color == "white":
			self.bg_code = 97
		elif bg_color == 0 or bg_color == "normal":
			self.bg_code = 0
		elif bg_color == 49:
			self.bg_code = 49

		else:
			raise BadColorError(bg_color)
		# format

		self.clean_format = []
		for f in format:

			if f not in self.clean_format:
				if f == 0 or f == f == "normal":
					self.clean_format.append(0)
				elif f == 1 or f == "bold":
					self.clean_format.append(1)
				elif f == 2 or f == "faint":
					self.clean_format.append(2)
				elif f == 3 or f == "italic":
					self.clean_format.append(3)
				elif f == 4 or f == "underline":
					self.clean_format.append(4)
				elif f == 5 or f == "slow_blink":
					self.clean_format.append(5)
				elif f == 6 or f == "rapid_blink":
					self.clean_format.append(6)
				elif f == 7 or f == "reverse":
					self.clean_format.append(7)
				elif f == 8 or f == "hidden":
					self.clean_format.append(8)
				elif f == 9 or f == "crossed":
					self.clean_format.append(9)
				elif f == 21 or f == "underline_bold":
					self.clean_format.append(21)
				elif f == 51 or f == "framed":
					self.clean_format.append(51)
				elif f == 52 or f == "rounded":
					self.clean_format.append(52)
				else:
					raise BadFormatError(f)

		self.fg_color = fg_color
		self.bg_color = bg_color
		self.returnv = returnv
		self.format = tuple(self.clean_format)
		self.end = end
