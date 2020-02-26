#!/usr/bin/python

import os
import colors
import analysers
import terminal

selected_analyzer = analysers.choice(
	message = 'Select a analyzer:'
)
superproject = input('What dir you wanna analyse?\n--> ')
print(
	colors.green,
	os.path.abspath(superproject),
	colors.reset_color
)

answer = input('Are you sure? ')
if answer.lower() in ['n', 'no']:
	exit()
terminal.break_line()

os.chdir(superproject)
directory_files = os.listdir()

for directory_file in directory_files:
	selected_analyzer(directory_file)

