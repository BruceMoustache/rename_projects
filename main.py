#!/usr/bin/python

import os
from empty import empty_analyser
import colors

TERMINAL_SIZE = os.get_terminal_size()

def break_line():
	global TERMINAL_SIZE
	print('-' * TERMINAL_SIZE.columns)

superproject = input('What dir you wanna analyse?\n--> ')
print(
	colors.green,
	os.path.abspath(superproject),
	colors.reset_color
)
# os.system(f'ls --color {superproject}')

answer = input('Are you sure? ')
if answer.lower() in ['n', 'no']:
	exit()
break_line()

os.chdir(superproject)
directory_files = os.listdir()

for directory_file in directory_files:
	empty_analyser(directory_file)

