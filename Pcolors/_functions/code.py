from ..exceptions import BadColorError, BadFormatError



def code(*id):
	"""
	generate an ANSI escape code composed of the parameters pased on id
	:param id: al SGR parameters included in the result
	:return: ANSI escape code
	"""
	cleared_ids = []
	final = ""
	for x in id:
		if x not in cleared_ids:

			if str(type(x)) == "<class 'tuple'>":
				for y in x:
					cleared_ids.append(y)
				continue
			cleared_ids.append(x)

	for i, x in enumerate(cleared_ids):


		if i == cleared_ids.__len__() - 1:
			final += str(x)
		else:
			final += str(x) + ";"
	final = f"\033[{final}m"
	return final
