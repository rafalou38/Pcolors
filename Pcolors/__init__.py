from colorama import init

init()

from . import shortcuts
from .style import style
from ._functions.prints import cprint
from ._functions.code import code
from ._functions.preview import preview


def to_bg(id):
	"""
	:param id: id of a color (light or dark)
	:return: id of the color for background
	"""
	return str(int(id) + 10)

