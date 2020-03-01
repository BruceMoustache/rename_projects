import os
import subprocess
from colors import *

terminal_size = os.get_terminal_size()

def break_line(fill='-', message=''):
	global terminal_size
	print(str.center(message, terminal_size.columns, fill))

def is_empty_directory(relative_path):
	if is_directory(relative_path):
		files_to_analyse = remove_unecessary_files_from_list(listdir(relative_path))
		return files_to_analyse == []
	return False

def is_directory(file_name):
	return os.path.isdir(file_name)

def remove_unecessary_files_from_list(directory_files):
	result = []
	for directory_file in directory_files:
		if not is_unecessary_file(directory_file):
			result.append(directory_file)
	return result

def is_unecessary_file(file_name):
	if file_name.startswith('.'):
		return True
	if file_name == '__pycache__':
		return True

def listdir(path='.', sort_by=None):
	# doesnt working
	#sort_key = lambda file_name: eval(f'os.stat(file_name).{sort_by}')
	sort_key = None
	return sorted(os.listdir(path), key=sort_key)

def run_command(command, return_binary_output=False):
	arguments = command.split()
	return subprocess.run(arguments, capture_output=return_binary_output).stdout

def show_content_of_command(command):
	binary_output = run_command(command, return_binary_output=True)
	return binary_output.decode('utf-8')

def modified_date(relative_path, time_format='%D'):
	run = f'date +"{time_format}" -r {relative_path}'
	return show_content_of_command(run).strip().replace('"', '').replace('/', '.')

def rename(old, new):
	print(f'renaming {blue}{old}...{reset_color}')
	os.rename(old, new)

