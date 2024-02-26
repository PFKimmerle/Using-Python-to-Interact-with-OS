#!/usr/bin/env python3

import sys
import csv

def populate_dictionary(filename):
  # initialize empty dictionary
  email_dict = {}
  # open csv file
  with open(filename) as csvfile:
  # read the csv file
    lines = csv.reader(csvfile, delimiter = ',')
    # loop over each line in csv
    for row in lines:
      # use name as the key and email as the value
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  try:
    # combine first and last name to form full name
    fullname = str(argv[1] + " " + argv[2])
    # populate dictionary with data from csv file
    # replace '<studentID>' with your ID
    email_dict = populate_dictionary('/home/<studentID>/data/user_emails.csv')
    # Find and return email
    return email_dict.get(fullname.lower())
  except IndexError:
    # if not enough command line arguments, return an error message
    return "Missing parameters"

def main():
  # call the find_email function with command line arguments
  # print results
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()