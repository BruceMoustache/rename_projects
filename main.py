#!/usr/bin/python

import os

BLUE = '\033[34m'
RESET_COLOR = '\033[m'

TERMINAL_SIZE = os.get_terminal_size()

def is_empty_directory(directory):
	# I need a name more clever
	true_files = remove_dotfiles(os.listdir(directory))
	return true_files == list()

def remove_dotfiles(directory_files):
	result = []
	for directory_file in directory_files:
		if not directory_file.startswith('.'):
			result.append(directory_file)
	return result

def break_line():
	global TERMINAL_SIZE
	print('-' * TERMINAL_SIZE.columns)

def rename_empty_project(directory):
	# to rename renamed projects
	name = directory.split('-')[0]  # dangerous
	new_name = f'{name}-(empty)'
	os.rename(directory, new_name)


superproject = input('What dir you wanna analyse?\n--> ')
print(os.path.abspath(superproject))
# os.system(f'ls --color {superproject}')

answer = input('Are you sure? ')
if answer.lower() in ['n', 'no']:
	exit()
break_line()

os.chdir(superproject)
directory_files = os.listdir()

for directory_file in directory_files:
	if os.path.isdir(directory_file) and is_empty_directory(directory_file):
		print(f'{BLUE}{directory_file}{RESET_COLOR} is empty, renaming..')
		rename_empty_project(directory_file)

