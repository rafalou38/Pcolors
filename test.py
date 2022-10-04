import math
import shutil
import timeit
from time import sleep
from typing import TextIO

import clipboard
import Pcolors
from Pcolors import style, cprint
import random
import sys

#
# class ProgressBar(object):
# 	"""
# 	fork of https://mike42.me/blog/2018-06-make-better-cli-progress-bars-with-unicode-block-characters
# 	"""
#
# 	def __init__(self, target: TextIO = sys.stdout):
# 		self._target = target
# 		self._text_only = not self._target.isatty()
# 		self._update_width()
#
# 	def __enter__(self):
# 		return self
#
# 	def __exit__(self, exc_type, exc_val, exc_tb):
# 		if exc_type is None:
# 			# Set to 100% for neatness, if no exception is thrown
# 			self.update(1.0)
# 		if not self._text_only:
# 			# ANSI-output should be rounded off with a newline
# 			self._target.write('\n')
# 		self._target.flush()
# 		pass
#
# 	def _update_width(self):
# 		self._width, _ = shutil.get_terminal_size((80, 20))
#
# 	def update(self, progress: float):
# 		# Update width in case of resize
# 		self._update_width()
# 		# Progress bar itself
# 		if self._width < 12:
# 			# No label in excessively small terminal
# 			percent_str = ''
# 			progress_bar_str = ProgressBar.progress_bar_str(progress, self._width - 2)
# 		elif self._width < 40:
# 			# No padding at smaller size
# 			percent_str = "{:6.2f} %".format(progress * 100)
# 			progress_bar_str = ProgressBar.progress_bar_str(progress, self._width - 11) + ' '
# 		else:
# 			# Standard progress bar with padding and label
# 			percent_str = "{:6.2f} %".format(progress * 100) + "  "
# 			progress_bar_str = " " * 5 + ProgressBar.progress_bar_str(progress, self._width - 21)
# 		# Write output
# 		if self._text_only:
# 			self._target.write(progress_bar_str + percent_str + '\n')
# 			self._target.flush()
# 		else:
# 			self._target.write('\033[G' + progress_bar_str + percent_str)
# 			self._target.flush()
#
# 	@staticmethod
# 	def progress_bar_str(progress: float, width: int):
# 		# 0 <= progress <= 1
# 		progress = min(1, max(0, progress))
# 		whole_width = math.floor(progress * width)
# 		remainder_width = (progress * width) % 1
# 		part_width = math.floor(remainder_width * 8)
# 		part_char = [" ", "▏", "▎", "▍", "▌", "▋", "▊", "▉"][part_width]
# 		if (width - whole_width - 1) < 0:
# 			part_char = ""
# 		line = "[" + "█" * whole_width + part_char + " " * (width - whole_width - 1) + "]"
# 		return line


from Pcolors.utils import square, de_ansify

# s = style(
# 				rgb_bg=[],
# 				rgb_fg=[]
# 			).get_code()
#
#
# print(s + square + " caca", end="")
#
# cprint("", 0, 0)
#
# print(
# 	de_ansify
# 		(
# 		s
# 	))

#
# fs.cprint(u.square * 4, "")
# fs_bold.cprint(u.square * 4)

# file.write(cprint("test 123", returnv=True))

s=Pcolors.builder.build("""
					<!--html-->
					<c underline >
						hello
						<c underline=false bold=false crossed/>
						not bold
					</c>
					""")
print(s)
# bar = f"""<c bold >|<c bold=false fg_color='yellow' />{"█"*50}<c fg_color='white' />{"░"*50}</c> """
#
# print(Pcolors.parser.build(bar, trim=False))

# p = ProgressBar()
# i = 0
# while i < 100:
# 	i += random.random()
# 	sleep(0.1)
# 	p.update(i / 100)
	# print("e")

# clipboard.copy(s.replace("#", "\033"))
# print(s)
# print(de_ansify(s))
