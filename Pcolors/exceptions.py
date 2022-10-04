class BadColorError(Exception):
	"""Exception raised when an unexpected value is paced in the fore.
	valid values:
		numbers   -> [90, 91, 92, 93, 94, 95, 96, 97, 30, 31, 32, 33, 34, 35, 36, 37]
		shortcuts ->Pcolors.shortcuts.dark.[any] Pcolors.shortcuts.light.[any]
		names     -> [black, red, green, yellow, blue, magenta, cyan, white]/[lblack, lred, lgreen, lyellow, lblue, lmagenta, lcyan, lwhite]


	Attributes:
		badValue -- bad input value
	"""

	def __init__(self, badValue):
		self.badValue = badValue


class BadFormatError(Exception):
	"""Exception raised when an unexpected value is paced in the fore.
	valid values:
		numbers   -> [0,1,2,3,4,5,6,7,8,9,21,51,52]
		shortcuts -> Pcolors.shortcuts.fore.[any]
		names     -> [rounded, framed, underline_bold, hidden, crossed, reverse, rapid_blink, slow_blink, underline, italic, faint, bold, normal]


	Attributes:
		badValue -- bad input value

	"""

	def __init__(self, badValue):
		self.badValue = badValue
