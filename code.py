import csv

# open up the file
with open('data/NBA1415GameLog.csv', 'rb') as csvfile:
	# parse the file using a dict reader. uses headers
	reader = csv.DictReader(csvfile)
	# for each line, print it out
	for line in reader:
		print(line["PLAYER FULL NAME"])