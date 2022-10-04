from html.parser import HTMLParser

from .._functions.helpers import base_format
from .._functions.prints import cprint
from .._functions.code import code
from ..shortcuts import format
from ..style import style
from ..exceptions import BadFormatError


# print(f'\x1b[2J\x1b[H')

class _color_parser(HTMLParser):
	def __init__(self,trim, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.trim = trim
		self.end_str = ""
		self.current_style = style()

	def handle_starttag(self, tag, attrs):
		for attr in attrs:
			if attr[0] == "fg_color":
				self.current_style.fg_color = attr[1]
			elif attr[0] == "bg_color":
				self.current_style.bg_color = attr[1]
			elif attr[0] == "rgb_bg":
				self.current_style.rgb_bg = attr[1][1:-1].split(",")
			elif attr[0] == "rgb_fg":
				self.current_style.rgb_fg = attr[1][1:-1].split(",")
			else:
				if attr[0] in base_format:
					if attr[1] != 'false':
						self.current_style.format.add(attr[0])
					else:
						self.current_style.format.remove(attr[0])
				else:
					raise BadFormatError(attr[0])
		self.end_str += code(0)
		self.end_str += self.current_style.get_code()

	def handle_startendtag(self, tag, attrs):
		# print("Encountered a start end tag:", tag)
		# print("attrs:", attrs)
		self.handle_starttag(tag, attrs)

	def handle_endtag(self, tag):
		# print("Encountered an end tag :", tag)
		print(tag)
		self.end_str += code(0);
		self.current_style.__init__()

	def handle_data(self, data: str):
		# print("Encountered some data  :", data)
		if self.trim:
			self.end_str += data.strip()
		else:
			self.end_str += data


def build(s, trim=True):
	cp = _color_parser(trim=trim)
	cp.feed(s)
	return cp.end_str
# if not "<" in s or not ">" in s:
# 	return s
# for char_i, char in enumerate(s):
# 	if char in ("<",">"):

# 		s = s.replace(char, "")
# return s
