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
	files 					= glob.glob(DATA_DIR+'/'+aname+'*.csv')
	if len(files) == 0:
		print('No such user exists')
		exit(2)
	else:
		print(files)


def get_data(list):

	records 				= []

	# Accessing each file to be retrieved
	for file in list:
		raw_data			= file.read()



# Constants and predefined variables
FILE_PATH 					= "../data/test.json"
DATA_DIR					= "../output"

request_data 				= get_request_data(FILE_PATH)
user_files					= get_data_list(request_data['uname'],DATA_DIR)
data 						= get_data(files)