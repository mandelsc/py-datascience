# py-datascience
A data science tutorial using NBA data

## Prerequisites
This tutorial assumes you have a basic, working knowledge of Python and of Git. In addition, you'll need to have the following installed on your computer:
- [Python 2.7](https://www.python.org/downloads/) (not 3.x!)
- [Git](https://msysgit.github.io/)
- A [GitHub account](https://github.com/join). There are some great tutorials on getting your computer setup with GitHub: https://help.github.com/articles/set-up-git/

## Preparation
### Fork the repository
Hit the fork button at the repository home (http://github.com/nsamala/py-datascience). This will give you a copy of the repository to mess around with as you please.

Once that is complete, make a note of the HTTPS clone url (found in the bottom right of the webpage for your forked repository) and run the following commands in a terminal on your computer:
```bash
git clone https://github.com/[YOUR USERNAME]/py-datascience.git && cd py-datascience
```

### Setup Travis CI (for unit testing)
As you complete programming assignments, you'll want to test them for correctness. We'll use Travis CI to automatically run tests against your code each time you push changes.
Go to [Travis CI](https://travis-ci.org) and login with your GitHub account. Hit the toggle switch next to py-datascience to enable builds for your repository.

## Run a test
If you trigger the code to build as is, it will fail. You can try this on the Travis CI interface. Let's get it working before we continue:
Add the following code to the `code.py` file:
```python
def add(x, y):
	return x + y

def increment(x):
	return add(x, 1)
	
def hello():
	return "world"
```

You can test these changes locally by running `python tests.py`. If everything went to plan, you should get 3 passed tests. Now push the changes to GitHub:

```bash
git add --all
git commit -m "passed the first test"
git push
```

You should see all of the tests pass in Travis CI.

## Next Steps
Awesome! Time to run to the first tutorial: [Loading + Parsing your data](lessons/LoadParseData.md)
