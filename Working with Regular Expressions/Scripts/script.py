#!/usr/bin/env python3

import re
import csv


# define function to cehck if email address contains a specific domain
def contains_domain(address, domain):
  # create regex pattern for domain
  domain = r'[\w\.-]+@'+domain+'$'
  # return True if address matches pattern
  if re.match(domain,address):
    return True
  return False

# define function to replace old domain in email with new domain
def replace_domain(address, old_domain, new_domain):
  # create regex pattern for old domain
  old_domain_pattern = r'' + old_domain + '$'
  # replace the old domain with new domain
  address = re.sub(old_domain_pattern, new_domain, address)
  return address

# main function where the program starts execution
def main():
  # set old and new domain names
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  # set the location of the CSV file with teh original emails
  # replace <studentID> csv_file_location, report_file
  csv_file_location = '/home/<studentID>/emails.csv'
  report_file = '/home/<studentID>/data' + '/updated_user_emails.csv'
  
  # initalize lists to hold email addresses
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []

  # read the CSV file and populate lists
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    # extract email addresses, stripping any whitespace
    user_email_list = [data[1].strip() for data in user_data_list[1:]]

    # go through emails and if they contain old domain
    # add them to the old_domain_email_list and replace domain
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)

    # find the index of the email address column
    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)

    # replace old domains with new domains in user data list
    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()

  # write the updated data to the report file
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()

main()