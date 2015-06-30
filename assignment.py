import csv

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

# Get the name of the first player in the file
def prob_02(data):
	
	return name
	
# Get the date on the last line in the file
def prob_03(data):
	
	return date
	
# Get the 100th player's name
def prob_04(data):
	
	return name

# Get a list of the unique OWN_TEAM elements in the file
def prob_05(data):
	teams = []
	
	return teams