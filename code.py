import csv

def read_file(filename):
	lines = []
	# open up the file
	with open(filename, 'rb') as csvfile:
		# parse the file	
		reader = csv.reader(csvfile)
		#reader = csv.DictReader(csvfile)
		
		# add each line into an array
		for line in reader:
			lines.append(line)
	return lines
	
def print_csv(data):
	for line in data:
	# When you change one of these lines, be sure to comment out the others so as to avoid duplicate print statements
		print line
		#print line[0]
		#print line["PLAYER FULL NAME"]

# comment out these lines before submitting the first assignment
data = read_file('data/NBA1415GameLog.csv')
print_csv(data)