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

data = read_file('data/NBA1415GameLog.csv')

# Return the number of lines in the data file (exclude the headers)
def prob_01(data):
	return len(data)
print(prob_01(data))

# Get the name of the first player in the file
def prob_02(data):
	return data[0]["PLAYER FULL NAME"]
print(prob_02(data))

# Get the date on the last line in the file

def prob_03(data):
	x = len(data) - 1 
	return data[x]["DATE"]
print(prob_03(data))

	
# Get the 100th player's name
def prob_04(data, n):
	return data[n-1]["PLAYER FULL NAME"]
print(prob_04(data,150))

##	for line in data:
##		if line == data["PLAYER FULL NAME"]:
##			name = line["99"]
##			return name
## print(prob_04(data))

# Get a list of the unique OWN_TEAM elements in the file



def prob_05(data):
	teams = []
	unique_list = set()
	unique_teams = []
	for row in data:
		teams.append(row["OWN TEAM"])
	unique_list = set(teams)
	unique_teams = list(unique_list)
	return unique_teams
print(prob_05(data))
