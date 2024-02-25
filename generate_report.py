
#!/usr/bin/env python3

# import the csv module to work with csv files
import csv

# define function to read employees from a csv file
def read_employees(csv_file_location):
# set up the csv dialect parameters
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
# open the csv file and read it into a dictionary
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  employee_list = []
# loop through the csv data, add each employee to a list
  for data in employee_file:
    employee_list.append(data)
  return employee_list
# call the read_employees function and print the result
# replace '<user_name>' with student ID
employee_list = read_employees('/home/<user_name>/employees.csv')
print(employee_list)

# define a function to prodess the employee list data
def process_data(employee_list):
  department_list = []
# create a list of departments from employee data 
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
# count how many employees are in each department
  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data
# process teh employee list to get data and print
dictionary = process_data(employee_list)
print(dictionary)

# define function to write the department data to a report
def write_report(dictionary, report_file):
  with open(report_file, "w+") as f:
  # write each department and count to the file
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()
# replace '<user_name>' with student ID
write_report(dictionary, '/home/<user_name>/report.txt')

