import renaming
import terminal

def undo_analyser(directory_file):
	if terminal.is_directory(directory_file):
		undo_renamer(directory_file)

def undo_renamer(directory):
	name = renaming.get_original_directory_name(directory)
	terminal.rename(directory, name)

