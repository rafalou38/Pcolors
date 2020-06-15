from ..exceptions import BadColorError, BadFormatError
from ..style import style
from .code import code



def cprint(text, fg_color=39, bg_color=49, end="\n", style=style(), format=(), returnv=False):
	# forground
	# light colors

	if fg_color == 39:
		fg_color = style.fg_color
	if bg_color == 49:
		bg_color = style.bg_color
	if format == ():
		format = style.format
	if end == "\n":
		end = style.end
	if not returnv:
		returnv = style.returnv

	if fg_color == 30 or fg_color == "lblack":
		fg_code = 30
	elif fg_color == 31 or fg_color == "lred":
		fg_code = 31
	elif fg_color == 32 or fg_color == "lgreen":
		fg_code = 32
	elif fg_color == 33 or fg_color == "lyellow":
		fg_code = 33
	elif fg_color == 34 or fg_color == "lblue":
		fg_code = 34
	elif fg_color == 35 or fg_color == "lmagenta":
		fg_code = 35
	elif fg_color == 36 or fg_color == "lcyan":
		fg_code = 36
	elif fg_color == 37 or fg_color == "lwhite":
		fg_code = 37

	# dark colors
	elif fg_color == 90 or fg_color == "black":
		fg_code = 90
	elif fg_color == 91 or fg_color == "red":
		fg_code = 91
	elif fg_color == 92 or fg_color == "green":
		fg_code = 92
	elif fg_color == 93 or fg_color == "yellow":
		fg_code = 93
	elif fg_color == 94 or fg_color == "blue":
		fg_code = 94
	elif fg_color == 95 or fg_color == "magenta":
		fg_code = 95
	elif fg_color == 96 or fg_color == "cyan":
		fg_code = 96
	elif fg_color == 97 or fg_color == "white":
		fg_code = 97
	elif fg_color == 0 or fg_color == "normal":
		fg_code = 0
	elif fg_color == 39:
		fg_code = 39

	else:
		raise BadColorError(fg_color)

	if bg_color == 30 or bg_color == "lblack":
		bg_code = 30
	elif bg_color == 31 or bg_color == "lred":
		bg_code = 31
	elif bg_color == 32 or bg_color == "lgreen":
		bg_code = 32
	elif bg_color == 33 or bg_color == "lyellow":
		bg_code = 33
	elif bg_color == 34 or bg_color == "lblue":
		bg_code = 34
	elif bg_color == 35 or bg_color == "lmagenta":
		bg_code = 35
	elif bg_color == 36 or bg_color == "lcyan":
		bg_code = 36
	elif bg_color == 37 or bg_color == "lwhite":
		bg_code = 37

	# dark colors
	elif bg_color == 90 or bg_color == "black":
		bg_code = 90
	elif bg_color == 91 or bg_color == "red":
		bg_code = 91
	elif bg_color == 92 or bg_color == "green":
		bg_code = 92
	elif bg_color == 93 or bg_color == "yellow":
		bg_code = 93
	elif bg_color == 94 or bg_color == "blue":
		bg_code = 94
	elif bg_color == 95 or bg_color == "magenta":
		bg_code = 95
	elif bg_color == 96 or bg_color == "cyan":
		bg_code = 96
	elif bg_color == 97 or bg_color == "white":
		bg_code = 97
	elif bg_color == 0 or bg_color == "normal":
		bg_code = 0
	elif bg_color == 49:
		bg_code = 49

	else:
		raise BadColorError(bg_color)


	clean_format = []
	for f in format:
		if f not in clean_format:
			if f == 0 or f == f == "normal":
				clean_format.append(0)
			elif f == 1 or f == "bold":
				clean_format.append(1)
			elif f == 2 or f == "faint":
				clean_format.append(2)
			elif f == 3 or f == "italic":
				clean_format.append(3)
			elif f == 4 or f == "underline":
				clean_format.append(4)
			elif f == 5 or f == "slow_blink":
				clean_format.append(5)
			elif f == 6 or f == "rapid_blink":
				clean_format.append(6)
			elif f == 7 or f == "reverse":
				clean_format.append(7)
			elif f == 8 or f == "hidden":
				clean_format.append(8)
			elif f == 9 or f == "crossed":
				clean_format.append(9)
			elif f == 21 or f == "underline_bold":
				clean_format.append(21)
			elif f == 51 or f == "framed":
				clean_format.append(51)
			elif f == 52 or f == "rounded":
				clean_format.append(52)
			else:
				raise BadFormatError(f)
	format=tuple(clean_format)

	

	if returnv:
		return f"{code(fg_code, bg_code + 10, format)}{text}\033[0m"
	print(f"{code(fg_code, bg_code + 10, format)}{text}\033[0m", end=end)

