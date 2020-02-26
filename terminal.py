import os

terminal_size = os.get_terminal_size()

def break_line(fill='-', message=''):
	global terminal_size
	print(str.center(message, terminal_size.columns, fill))

def not_implement(module):
	print(f'The {module} has not implement yet. Exiting...')
	exit()

