import time

from ._functions import console, prints

empty_block = "\u2588"
square = empty_block * 2

def wait(name, seconds):
	first = True
	while seconds >= 0:
		if not first:
			console.cursor.move_up(1)
		first = False
		prints.cprint(name + " : ", "cyan", end="")
		prints.cprint(str(seconds)[:3] + "    ", "magenta", format=("bold",))
		seconds -= 0.1
		time.sleep(0.1)

	console.cursor.move_up(1)
	prints.cprint(name + " : ", "cyan", end="")
	prints.cprint("finish  \n", "green", format=("bold",))


def de_ansify(string: str):
	string = string.encode('ascii').replace(b"\x1b",b"#")
	return string.decode("unicode_escape")
