#!/usr/bin/env python3

import sys
import os
import re

# function searches for given error in log file
def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  # open the log file and interate through each line
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      # build a regex pattern for each word in error description
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      # if all parts of the error are found, add to log and return error
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors

# this fucntion writes the found errors to an output file  
def file_output(returned_errors):
  # save the errors to a file 
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()

# main block to execute the functions above
if __name__ == "__main__":
  log_file = sys.argv[1]
  # serach for errors
  returned_errors = error_search(log_file)
  # write the errors to output file
  file_output(returned_errors)
  # exit script
  sys.exit(0)