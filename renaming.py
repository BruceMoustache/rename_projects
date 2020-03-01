import config

def get_original_directory_name(directory):
	return directory.split(config.rename_separator)[0]

