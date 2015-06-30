# Lesson 1: Loading + Parsing your data

## Preparation
To get the code for this tutorial, you'll need to change to the lesson-01 branch of this repository. To do so:
```bash
git checkout -f lesson-01
```

Note: Keep in mind that running this command does flush out any changes you've made to this directory. If you've run some experiments that you want to store, you'll want to commit those changes to your current branch.

## Introduction
The first big step with any data science experiment is ensuring you have data to work with! For the purposes of this lesson, we'll be using the NBA 2014-2015 Game Log dataset (found in the /data folder of your repository).


### Reading and printing out data
Python has an awesome built-in CSV reader that we'll use to read in the file. For starters, let's read in each line and spit it right back out on the terminal. Open up your code.py and add the following code:

```python
import csv

# open up the file
with open('data/NBA1415GameLog.csv', 'rb') as csvfile:
	# parse the file	
	reader = csv.reader(csvfile)
	# for each line, print it out
	for line in reader:
		print line
```

Once you run `python code.py`, you should see endless lines of NBA player stats printed out to your console.

### Accessing data features
Now that you can access the data in-memory, we'll want to be able to easily manipulate it. 

Let's start with a demo by printing out just the player names. Change the `print ', '.join(log)` to `print log[2]` and run code.py. You should get a list of player names. When the CSV parser reads in a line, it breaks it down into an array by the comma separator.

As your data grows or changes, you might have different fields or ordering to your data. Also, somehow remembering that `log[2]` refers to player names is not easy when you have hundreds of lines of code. Instead, let's use another wonderful feature of python's csv reader: we can read each line into an object defined by the headers.

```python
import csv

# open up the file
with open('data/NBA1415GameLog.csv', 'rb') as csvfile:
	# parse the file using a dict reader
	reader = csv.DictReader(csvfile)
	# for each line, print it out
	for line in reader:
		print line
```

Now when you run the code, each line will be attributed with the headers. This gives us a super easy way to access the data. Now, you can change `print(line)` to `print(line["PLAYER FULL NAME"])` to print out player names.





 
