# from colorama import init

# init()

import atexit

from . import shortcuts
from .style import style, inputStyle
from ._functions.prints import cprint, cget, cinput
from ._functions.code import code
from ._functions.preview import preview
from ._functions import console
from .builder import parser

reset_color = lambda: print('\x1b[0m', end="")

def to_bg(id):
	"""
	:param id: id of a fore (light or dark)
	:return: id of the fore for background
	"""
	return str(int(id) + 10)

def _exit():
	reset_color()

atexit.register(_exit)
