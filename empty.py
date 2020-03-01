import terminal
import renaming

def empty_analyser(directory_file):
	if terminal.is_empty_directory(directory_file):
		rename_empty_project(directory_file)

def rename_empty_project(directory):
	name = renaming.get_original_directory_name(directory)
	new_name = f'{name}-(empty)'
	terminal.rename(directory, new_name)

