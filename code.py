import csv
#from datetime import datetime, date

#start = date(2015, 2, 1)
#end = date(2015, 2, 28)

def read_file(filename):
	lines = []
	# open up the file
	with open(filename, 'rb') as csvfile:
		# parse the file	
		#reader = csv.reader(csvfile)
		reader = csv.DictReader(csvfile)
		
		# add each line into an array
		for line in reader:
			lines.append(line)
	return lines

def filter_date(strDate, start, end):
  #convert to date
  converted = datetime.strptime(strDate, "%m/%d/%Y").date()
  
  #filter by start and end
  return converted >= start and converted <= end
  
# read the data file
data = read_file("data/NBA1415GameLog.csv")

# apply the name filter using a list comprehension
fournier_data = [line for line in data if line["PLAYER FULL NAME"] == "Evan Fournier"]
print fournier_data

# calculate the mean of the data
#fournier_mean = sum(fournier_data) / len(fournier_data)
#print sum(fournier_data)
#print fournier_mean

# date sample
#print datetime.strptime(data[0]["DATE"], "%m/%d/%Y")

# Filter / Map / Reduce Method
# apply the name filter
#fournier_data = filter(lambda d: d["PLAYER FULL NAME"] == "Evan Fournier", data)
# apply the date filter
#fournier_data = filter(lambda d: filter_date(d["DATE"], start, end), fournier_data)
# use the map function to get all points
#fournier_pts = map(lambda d: float(d["PTS"]), fournier_data)
# use the reduce function to give us the sum of points in order to get the average
#fournier_mean = reduce(lambda x, y: x + y, fournier_pts) / len(fournier_pts)

#print fournier_pts
#print "average:", fournier_avg