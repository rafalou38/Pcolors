from ._functions.helpers import hex_to_rgb
from .exceptions import BadColorError, BadFormatError
from ._functions.code import code
from ._functions.helpers import hex_to_rgb
from .exceptions import BadColorError


class style(object):
	def cprint(self, text, end="\n"):
		# here to avoid circular dependency
		from ._functions.prints import cprint
		cprint(text, style=self, end=end)

	def cget(self, text, end="\n"):
		# here to avoid circular dependency
		from ._functions.prints import cget
		return cget(text, style=self, end=end)

	def get_code(self):
		self.update()
		a = code(self.fg_code, self.bg_code, self.format_codes, self.rgb_bg_code, self.rgb_fg_code)
		return a

	def update(self):
		# here to avoid circular dependency
		from ._functions.helpers import get_format_code, get_color_code
		self.rgb_fg_code = self.rgb_fg[:]
		self.rgb_bg_code = self.rgb_bg[:]
		self.format_codes = set()
		self.fg_code, self.bg_code = 0, 0

		if self.rgb_bg != []:
			if isinstance(self.rgb_bg, str):
				try:
					self.rgb_bg_code = hex_to_rgb(self.rgb_bg)
					self.rgb_bg_code.insert(0, 48)
				except ValueError:
					raise BadColorError(self.rgb_bg) from None
				# pass
			elif len(self.rgb_bg) == 3:
				self.rgb_bg_code.insert(0, 48)
			else:
				raise BadColorError(self.rgb_bg)

		if self.rgb_fg != []:
			if isinstance(self.rgb_fg, str):
				try:
					self.rgb_fg_code = hex_to_rgb(self.rgb_fg)
					self.rgb_fg_code.insert(0, 38)
				except ValueError:
					raise BadColorError(self.rgb_fg) from None
			elif len(self.rgb_fg) == 3:
				self.rgb_fg_code.insert(0, 38)
			else:
				raise BadColorError(self.rgb_fg)


		if not isinstance(self.fg_code, int):
			self.fg_code = 10
		self.fg_code = get_color_code(self.fg_color)

		if not isinstance(self.bg_color, int):
			self.bg_code = 10
		self.bg_code += get_color_code(self.bg_color)

		for f in self.format:
			self.format_codes.add(get_format_code(f))

	def __init__(self, fg_color=39, bg_color=49, rgb_bg=None, rgb_fg=[], end="\n", format=None):
		if rgb_bg is None:
			rgb_bg = []
		if format is None:
			format = set()

		self.rgb_fg = rgb_fg
		self.rgb_bg = rgb_bg
		self.rgb_fg_code = rgb_fg
		self.rgb_bg_code = rgb_bg
		self.fg_color = fg_color
		self.bg_color = bg_color
		self.fg_code = 0
		self.bg_code = 0
		self.format = format
		self.format_codes = set()
		self.end = end
		self.update()

class inputStyle():
	def __init__(self, prompt_style=None, response_style=None):
		if not prompt_style:
			prompt_style = style()
		if not response_style:
			response_style = style()

		self.prompt_style=prompt_style
		self.response_style=response_style

	def cinput(self, prompt, finish="below"):
		from ._functions.prints import cinput

		self.prompt_style.update()
		self.response_style.update()
		return cinput(prompt, self.prompt_style, self.response_style)

