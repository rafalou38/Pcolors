def move_up(e)        : print(f'\x1b[{e}A', end = "")
def move_left(e)      : print(f'\x1b[{e}D', end = "")
def move_down(e)      : print(f'\x1b[{e}B', end = "")
def move_right(e)     : print(f'\x1b[{e}C', end = "")

def hide()       : print(f'\x1b[?25l', end = "")
def show()       : print(f'\x1b[?25h', end = "")

def save_pos()   : print(f'\x1b[s', end    = "")
def restore_pos(): print(f'\x1b[u', end    = "")

def reset()      : print(f'\x1b[H', end    = "")
def set_pos(cls,x,y):
	"""
	change cursor position absolute or relative to current


	preview:
				~1
				y 
				|                         
		-1 x---O---x ~1                           
				| 
				y 
			~-1
	use ~ for relative move:
		cursor_pos("~4","~-5")
		move 4 right and 5 down
	use direct numbers for absolute move:
		cursor_pos(4,5)
		set cursor pos to 4,5

	Warning:
		You can't mix relative and absolute


	Args:
		x (int/str): collumn
		y (int/str): row
	"""    
	if isinstance(x, int): # x = absolute position
		if isinstance(y, int):
			print(f"\x1b[{x};{y}H", end="")
		else: raise ValueError("you can only use rel or absolute but not mixed")

	elif isinstance(x, str):
		if x[0] == "~": # x = relative position
			if y[0] == "~":
				x = int(x[1:])
				y = int(y[1:])
				if x > 0:
					move_right(abs(x))
				else:
					move_left(abs(x))
				if y > 0:
					move_up(abs(y))
				else:
					move_down(abs(y))
			else: raise ValueError("you can only use rel or absolute but not mixed")