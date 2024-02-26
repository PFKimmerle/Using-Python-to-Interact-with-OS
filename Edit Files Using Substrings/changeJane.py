#!/usr/bin/env python3

# Import the sys module to access command line arguments and subprocess to run shell commands
import sys
import subprocess

# Open file with the name provided as the first command line argument
f = open(sys.argv[1], "r")

# Read each line of file
for line in f.readlines():
  # Strip whitespace from the beginning and end of the line to get the old filename
  old_name = line.strip()
  # Replace the substring 'jane' with 'jdoe' to get the new filename
  new_name = old_name.replace("jane", "jdoe")
  # Use the subprocess module to run the 'mv' command which renames the file
  subprocess.run(["mv", old_name, new_name])

# Close the file 
f.close()
