import numpy
import json
import os
import glob

# Accessing the login request details
def get_request_data(file):

	# Accessing current login request data
	try:
		with open(file,'r') as infile:
			data			= json.load(infile)

		# Deleting the file after reading it's contents
		# os.remove(file)

		return data

	except IOError:
		print('File not found')
		exit(1)


# Accessing the datasets for a user
def get_data_list(aname,directory):

	# Checking for all names in the data directory
	files 					= glob.glob(DATA_DIR+'/'+aname+'.csv')
	if len(files) == 0:
		exit(2)

	return files[0]


# Accessing the keystroke data of the specified user
def get_data(file):

	records 				= []
	# Accessing each file to be retrieved
	with open(file,'r') as infile:
		raw_data			= infile.read()

	# Seperating each entry
	records 				= raw_data.split('\n')
	return records


def format_data(data):

	# Creating strucutes for various datasets
	formatted_data 			= []
	size 					= len(data[0].split(','))
	for i in range(size):
		formatted_data.append([])
	for entry in data:
		items 				= entry.split(',')
		for i in range(size):
			formatted_data[i].append(items[i])

	print(formatted_data)
	return formatted_data

# Constants and predefined variables
FILE_PATH 					= "../data/test.json"
DATA_DIR					= "../output"

request_data 				= get_request_data(FILE_PATH)
user_file					= get_data_list(request_data['uname'].lower(),DATA_DIR)
raw_data 					= get_data(user_file)
formatted_data 				= format_data(raw_data)