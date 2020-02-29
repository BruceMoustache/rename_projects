import terminal
import colors
import os
from empty import remove_dotfiles

def time_analyzer(directory):
	# terminal.not_implement('time analyzer')
	if os.path.isdir(directory):
		filename = "teste.txt"
		# Command shell to get last date of alteration within folder
		# Save output of command an variable $(filename)
		command = "date --reference="+directory+" +%d/%m/%y > "+filename
		os.system(command)
		# Read output
		date = read_output(filename)
		print(f'{colors.blue}{directory}{colors.reset_color} was changed in: {colors.green}{date}{colors.reset_color}...')

def time_analyzer_without_empty(directory):
	terminal.not_implement('time analyzer without empty')

# Function responsible for reading output in variable $(filename)
def read_output(filename):
	file = open(filename, "r")
	date = []
	for line in file:
		date.append(line)

	file.close()
	date = date[0].split("\n")
	return date[0]
