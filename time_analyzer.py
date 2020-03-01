import renaming
import terminal

def time_analyzer(path):
	if terminal.is_directory(path):
		time_renamer(path)

def time_analyzer_without_empty(path):
	if terminal.is_directory(path) and not terminal.is_empty_directory(path):
		time_renamer(path)

def time_renamer(old_name):
	name = renaming.get_original_directory_name(old_name)
	modified_date = terminal.modified_date(old_name, time_format="%m.%d")
	new_name = f'{name}-({modified_date})'
	terminal.rename(old_name, new_name)

