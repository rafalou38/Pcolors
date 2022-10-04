from .code import code
from ..style import style as style_class


def cprint(text, fg_color=39, bg_color=49, format=None, end="\n", style=None):
	if not style:
		style = style_class(fg_color=fg_color, bg_color=bg_color, format=format, end=end, )

	print(f"{style.get_code()}{text}\033[0m", end=end)

	return style


def cget(text, fg_color=39, bg_color=49, format=None, end="\n", style=None):
	if not style:
		style = style_class(fg_color=fg_color, bg_color=bg_color, format=format, end=end, )

	return f"{style.get_code()}{text}\033[0m" + end


def cinput(prompt, prompt_style=None, response_style=None, end=lambda r: "\n"):
	if not prompt_style:
		prompt_style = style_class()

	if not response_style:
		response_style = style_class()

	prompt_style.cprint(prompt, end="")

	print(response_style.get_code(), end="")

	r = input()

	print(code(0), end="")


	return r
