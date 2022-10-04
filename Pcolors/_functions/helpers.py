from ..exceptions import BadColorError, BadFormatError

base_colors = {
	"black": 30,
	"red": 31,
	"green": 32,
	"yellow": 33,
	"blue": 34,
	"magenta": 35,
	"cyan": 36,
	"white": 37,
}
base_format = {
	"normal": 0,
	"bold": 1,
	"faint": 2,
	"italic": 3,
	"underline": 4,
	"slow_blink": 5,
	"rapid_blink": 6,
	"reverse": 7,
	"hidden": 8,
	"crossed": 9,
	"underline_bold": 21,
	"framed": 51,
	"rounded": 52,
}
valid_attrs = [
	"normal",
	"bold",
	"faint",
	"italic",
	"underline",
	"slow_blink",
	"rapid_blink",
	"reverse",
	"hidden",
	"crossed",
	"underline_bold",
	"framed",
	"rounded",
]


def _remove_prefix(self: str, prefix: str) -> str:
	if self.startswith(prefix):
		return self[len(prefix):]
	else:
		return self[:]


def _remove_suffix(self: str, suffix: str) -> str:
	if suffix and self.endswith(suffix):
		return self[:-len(suffix)]
	else:
		return self[:]


def hex_to_rgb(value):
	h = _remove_prefix(value, "#")
	if len(h) != 6:
		raise BadColorError(value)
	return list(int(h[i:i + 2], 16) for i in (0, 2, 4))


def get_color_code(color):
	if isinstance(color, str):
		code = 0
		if color.startswith("l"):
			code += 60
			color = _remove_prefix(color, "l")
		if color in base_colors:
			code += base_colors[color]
		else:
			raise BadColorError(color)
	else:
		code = color
	return code


def get_format_code(formats):
	if isinstance(formats, str):
		code = 0
		if formats in base_format:
			code += base_format[formats]
		else:
			raise BadFormatError(formats)
	else:
		code = formats
	return code
