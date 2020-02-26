import os
import colors

def empty_analyser(directory_file):
	if os.path.isdir(directory_file) and is_empty_directory(directory_file):
		print(f'{colors.blue}{directory_file}{colors.reset_color} is empty, renaming...')
		rename_empty_project(directory_file)

def rename_empty_project(directory):
	# to rename renamed projects
	name = directory.split('-')[0]  # dangerous
	new_name = f'{name}-(empty)'
	os.rename(directory, new_name)

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

