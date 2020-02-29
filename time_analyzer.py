import terminal
import colors
import os
from empty import remove_dotfiles

def time_analyzer(directory):
	# terminal.not_implement('time analyzer')
	if os.path.isdir(directory):
		filename = "teste.txt"
		command = "ls -l "+directory+" > "+filename
		date = read_output(filename)
		print(f'{colors.blue}{directory}{colors.reset_color} was changed in: {colors.green}{date}{colors.reset_color}...')

def time_analyzer_without_empty(directory):
	terminal.not_implement('time analyzer without empty')

def read_output(filename):
	file = open(filename, "r")
	date = []
	for line in file:
		date.append(line)

	file.close()
	date = date[0].split("\n")
	return date[0]
