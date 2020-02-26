import terminal

from empty import empty_analyser
from time_analyzer import time_analyzer
from time_analyzer import time_analyzer_without_empty

def choice(message=None):
	global MAP_NAME_TO_ANALYZER

	if not message is None:
		print(message)

	# print(MAP_NAME_TO_ANALYZER)  # debug
	analysers_keys = list(MAP_NAME_TO_ANALYZER.keys())
	for index, analyser in enumerate(analysers_keys):
		print(f'[{index}] - {analyser}')

	selected_index = int(input('--> '))
	selected_key = analysers_keys[selected_index]
	selected_analyser = MAP_NAME_TO_ANALYZER[selected_key]

	return selected_analyser

def all_analysers(directory):
	global MAP_NAME_TO_ANALYZER

	my_map = MAP_NAME_TO_ANALYZER.copy()
	del my_map['all']

	for analyser in my_map.values():
		analyser(directory)

MAP_NAME_TO_ANALYZER = {
	'all': all_analysers,
	'empty': empty_analyser,
	'time': time_analyzer,
	'time (expect empty dirs)': time_analyzer_without_empty,
}

