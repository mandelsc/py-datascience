import csv

# open up the file
with open('data/NBA1415GameLog.csv', 'rb') as csvfile:
	# parse the file	
	reader = csv.reader(csvfile)
	#reader = csv.DictReader(csvfile)
	# for each line, print it out
	for line in reader:
# When you change one of these lines, be sure to comment out the others so as to avoid duplicate print statements
		print line
		#print line[0]
		#print line["PLAYER FULL NAME"]