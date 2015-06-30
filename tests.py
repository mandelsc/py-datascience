import unittest
import code

class TestIntroduction(unittest.TestCase):
  def test_add(self):
      self.assertEqual(code.add(1, 2), 3)

  def test_increment(self):
      self.assertTrue(code.increment(1), 2)
      
  def test_hello(self):
      self.assertTrue(code.hello(), "world")

if __name__ == '__main__':
    unittest.main()