#!/usr/bin/env python3

# import unitest module to conduct automated test
import unittest
# import find_email function from emails module
from emails import find_email

# define class to inherit from unittest. Testcase to create test cases
class EmailsTest(unittest.TestCase):
  # define test case method to test behavior of find_email
  def test_basic(self):
    # define a test case list simulating command line arguments
    testcase = [None, "Bree", "Campbell"]
    # define the expected reuslt for test case
    expected = "breee@abc.edu"
    # assert result from find_email matches the expected result
    self.assertEqual(find_email(testcase), expected)

  # define a test case method to test behavior of find_email
  # when only one name is given
  def test_one_name(self):
    # define a test case list with only one name
    testcase = [None, "John"]
    # define the expected result for this test case (error message)
    expected = "Missing parameters"
    # assert result from find_email matches expected error message
    self.assertEqual(find_email(testcase), expected)

  # define a test case method to test behavior of find_email 
  # when no matching email is found
  def test_two_name(self):
    # define a test case list with a full name
    testcase = [None, "Roy","Cooper"]
    # define expected result for test case (no email found)
    expected = "No email address found"
    # assert that result from find_email matches expected result
    self.assertEqual(find_email(testcase), expected)

if __name__ == '__main__':
  unittest.main()