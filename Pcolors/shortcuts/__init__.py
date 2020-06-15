from . import dark, light, format

def to_bg(id):
	"""
	:param id: id of a color (light or dark)
	:return: id of the color for background
	"""
	return str(int(id) + 10)