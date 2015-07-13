# Lesson 2: Analyzing the data

## Preparation
To get the code for this tutorial, you'll need to change to the lesson-02 branch of this repository. To do so:
```bash
git checkout -f lesson-02
```

## Lesson
### Filtering the data
Now that you have some data to mess around with, let's get to the fun part: analysis! For starters, let's first select all of Evan Fournier's games for the 2014-2015 season. In the previous lesson, we learned how to select data based off of a field name. This time around, we need to select *all* items that match our query.

To do so, we'll use a list comprehension:

```python
fournier_data = [line for line in data if line["PLAYER FULL NAME"] == "Evan Fournier"]
```

List comprehensions give us the power of a for loop in a nice, easy to read expression. Broken down, this reads:
*return each line in data where the field __PLAYER FULL NAME__ is __Evan Fournier__*

Instead of returning the entire line object, we can also opt, to return a specific field in `line` each time. Modify the code to the following:

```python
fournier_data = [line["PTS"] for line in data if line["PLAYER FULL NAME"] == "Evan Fournier"]
```

`fournier_data` should now list out all of the points that Evan Fournier scored in the 2014 - 2015 season. Time to get our first average!

### Data Transformation + Analysis
Uncomment out the following lines:
```python
fournier_mean = sum(fournier_data) / len(fournier_data)
print fourier_mean
```

Ahhh! That last line didn't work too well, did it?
```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Let's try to debug this. Comment out `fournier_mean = sum(fournier_data) / len(fournier_data)` and uncomment out the line that says `print sum(fournier_data)` and run it again. Same error. What happened? 

When we read in the data using the `csv.DictReader` in the first lesson, we blindly read in the data. To Python, it's going to assume that all of this data is a string because...well the file is stored as a text string. We need to parse this data into a number before we can do anything to it. Change the code to the following:

```python
fournier_data = [float(line["PTS"]) for line in data if line["PLAYER FULL NAME"] == "Evan Fournier"]
```

The sum should be printed out this time around, great! Our simple fix will be to convert each item to a number within our list comprehension. Revert the commented lines to their original state:

```python
fournier_mean = sum(fournier_data) / len(fournier_data)
#print sum(fournier_data)
```

Sweet, we finally have that average! Obviously, this type of conversion doesn't scale as we a lot of fields. You'll see a more elegant way to fix this later on. Right now, let's add more filters to our data!

### Filtering by date

We'll be tapping into python date library to give us a bit more power. Uncomment the following line from the top of your code file:

```python
from datetime import datetime, date
```

Before we can add any filtering by date, we'll need to convert the date strings into a binary object for Python to understand. In the CSV file, the dates are in the format M/D/YYYY. Since this is consistent, we'll take advantage of that when parsing our dates. Uncomment out the following line to get the date on the first line in the file:

```python
print datetime.strptime(data[0]["DATE"], "%m/%d/%Y")
```

*Note*: The casing of the date format DOES matter. The [Python documentation](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior) has a full listing of the different datetime identifiers you can use to extract parts of a datetime object from a string.

Combine this new knowledge with the filtering we learned previously. Extend the previous points average example to only consider games in February. Uncomment the following code:

```python
start = date(2015, 2, 1)
end = date(2015, 2, 28)
```

While you're at it, take a look at the filter_date function:
```python
def filter_date(strDate, start, end):
  #convert to date
  converted = datetime.strptime(line["DATE"], "%m/%d/%Y").date()
  return converted >= start and converted <= end
```
This function will return a true/false boolean based on whether or not a date falls in the start and end parameters. We can add filter to the existing list comprehension:
```python
fournier_data = [float(line["PTS"]) for line in data if line["PLAYER FULL NAME"] == "Evan Fournier" and filter_date(line["DATE"]]
```

### Summary
Now you have the basic tools to do your own analysis in Python! Here's what you learned:
- Filter data using a list comprehension
- Sanitizing and transforming data to the proper format
- Basic debugging (ish)
- Use of the datetime library to parse and interact with dates
- Apply multiple filters to a list comprehension

That's quite a bit. However, before the assignment, let's look at an alternative approach to doing this data manipulation: filter(), map(), and reduce().

### Filter / Map / Reduce
Stub to add in brief introduction to filter(), map(), reduce() and lambda functions 

## Progamming Assignment
As before, the assignment for this lesson is in assignments.py. This time around, you'll have a couple recap assignments to refresh your memory. When complete, run it against `python tests.py` to ensure your code works properly. Push to GitHub and test in Travis CI to ensure everything works.