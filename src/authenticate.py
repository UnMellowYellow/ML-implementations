import numpy as np
import json
import os
import glob
import scipy.linalg

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

	# No user with the given username exists
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
			formatted_data[i].append(float(items[i]))

	return formatted_data

def get_test_features(something):

	# Generating feature values
	features 				= []
	for i in range(1,len(something)):
		features.append(something[i]["timeDown"]-something[i-1]["timeUp"])

	return features

# Constants and predefined variables
FILE_PATH 					= "../data/test.json"
DATA_DIR					= "../output"
request_data 				= get_request_data(FILE_PATH)
user_file					= get_data_list(request_data['uname'].lower(),DATA_DIR)
raw_data 					= get_data(user_file)
formatted_data 				= format_data(raw_data)
covariance 					= np.cov(formatted_data)
new_covariance_metric		= scipy.linalg.inv(scipy.linalg.sqrtm(covariance))
# transpose					= np.transpose(new_covariance_metric)
print(new_covariance_metric)
average_feature_value 		= []
for values in formatted_data:
	average_feature_value.append(np.average(values))
print(average_feature_value)
test 						= get_test_features(request_data['features'])
print(test)
resultant 					= []
for i in range(len(average_feature_value)):
	resultant.append(average_feature_value[i]-test[i])

print(resultant)
print(np.dot(new_covariance_metric,resultant))