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
Python has an awesome built-in CSV reader that we'll use to read in the file. For starters, let's read in each line and spit it right back out on the terminal. Open up your code.py and you should see the following code:

```python
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
```

Once you run `python code.py`, you should see endless lines of NBA player stats printed out to your console.

### Accessing data features
Now that you can access the data in-memory, you'll want to be able to easily manipulate it. 

Let's start with a demo by printing out just the player names. In the print_csv function, comment out `print line` and uncomment `print line[2]`. You should get a list of player names. This happens because the CSV reader breaks down each record into array split by the comma.

As your data grows or changes, you might have different fields or ordering to your data. Somehow remembering that `line[2]` refers to player names is not easy when you have hundreds of lines of code. Instead, let's use another wonderful feature of python's csv reader: read the data into a dictionary tokenized by the header columns.

Comment out the `reader = csv.reader(csvfile)` and uncomment `reader = csv.DictReader(csvfile)`. This tells the parser to treat each record as a key-value dictionary.

```python
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
```

When you run the code this time, each line will be attributed with the headers. This gives us a super easy way to access the data. Comment out `print(line)` and uncomment `print(line["PLAYER FULL NAME"])` to print out player names.

## Progamming Assignment
You'll find the first programming assignment in the assignment.py file. There are a number of problems for you to complete. When complete, run it against `python tests.py` to ensure your code works properly. When complete push it to Travis CI to confirm everything works.