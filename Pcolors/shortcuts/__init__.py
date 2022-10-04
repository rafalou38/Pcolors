from . import dark, light, format

def to_bg(id):
	"""
	:param id: id of a fore (light or dark)
	:return: id of the fore for background
	"""
	return str(int(id) + 10)