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
	count = 0
 	for row in data:
  		count += 1
 	return count
print(prob_01(data))

# Get the name of the first player in the file
def prob_02(data):
	for line in data:
 		name = line["PLAYER FULL NAME"]
 		return name
print(prob_02(data))

# Get the date on the last line in the file
def prob_03(data):
	for line in data:
		date = line["DATE"]
	return date
print(prob_03(data))

	
# Get the 100th player's name
def prob_04(data):
	for line in data:
		if line == data[99]:
			name = line["PLAYER FULL NAME"]
			return name
print(prob_04(data))



##	for line in data:
##		if line == data["PLAYER FULL NAME"]:
##			name = line["99"]
##			return name
## print(prob_04(data))

# Get a list of the unique OWN_TEAM elements in the file


	
def prob_05(data):
	unique_teams = []
	unique_list = set()
	teams = []
	for row in data:
		unique_teams.append(row["OWN TEAM"])
	unique_list = set(unique_teams)
	teams = list(unique_list)
	return teams
print(prob_05(data))
