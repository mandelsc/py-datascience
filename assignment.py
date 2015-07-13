import csv

# In this assignment, tests.py will use the read_file function listed below
# and provide you with the data for each of the problems. Be sure to review
# how to access data fields by column header from the lesson in order to
# to complete the assignment.

def read_file(filename):
	lines = []
	with open(filename, 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for line in reader:
			lines.append(line)
	return lines
	
def print_csv(data):
	for line in data:
		print line

# Return the number of lines in the data file (exclude the headers)
def prob_01(data):
	
	return count

# Get the name of the first player in the file using the column name (PLAYER FULL NAME)
def prob_02(data):
	
	return name
	
# Get the date on the last line in the file using the column name (DATE)
def prob_03(data):
	
	return date
	
# Get the 100th player's name using the column name (PLAYER FULL NAME)
def prob_04(data):
	
	return name

# Get an array of the unique OWN_TEAM elements in the file
def prob_05(data):
	teams = []
	
	return teams