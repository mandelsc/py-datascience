import unittest
import assignment

class TestLesson1(unittest.TestCase):
  # reads in the NBA stats as an array of key-values into data
  data = assignment.read_file('data/NBA1415GameLog.csv')
  
  # the correct answer to problem 5 will return this array
  unique_teams = ['Orlando', 'New Orleans', 'Dallas', 'San Antonio', 'Houston', 'LA Lakers', 'Milwaukee', 'Charlotte', 'Philadelphia', 'Indiana', 'Brooklyn', 'Boston', 'Washington', 'Miami', 'Atlanta', 'Toronto', 'Minnesota', 'Memphis', 'Chicago', 'New York', 'Detroit', 'Denver', 'Utah', 'Phoenix', 'Golden State', 'Sacramento', 'Oklahoma City', 'Portland', 'Cleveland', 'LA Clippers']
  
  # in each of the following unit tests, we'll pass in the data from the CSV file as an array
  def test_count_lines(self):
      self.assertEqual(assignment.prob_01(self.data), 27633)
      
  def test_first_line_name(self):
      self.assertEqual(assignment.prob_02(self.data), "Tobias Harris")
      
  def test_last_line_date(self):
      self.assertEqual(assignment.prob_03(self.data), "6/16/2015")
  
  def test_100th_line_name(self):
      self.assertEqual(assignment.prob_04(self.data), "CJ Miles")
      
  def test_unique_teams(self):
      self.assertEqual(assignment.prob_05(self.data), self.unique_teams)

if __name__ == '__main__':
    unittest.main()