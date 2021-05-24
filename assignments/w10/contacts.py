# contacts.py
# program:  Read contact info and store in a file.
# 
# usage:    Checks that file does not exist, writes as a csv.
#
# Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.
import os.path
from os import path

__user_dir__ = input("Enter directory name, to save file: \n")
__user_filename__ = input("Enter file name with extension, to be saved: \n")
__user_file__ = os.path.join(__user_dir__, __user_filename__)

# __user_file__ = open(__user_file_input__, "r")
# Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.  

try:
    os.path.exists(__user_file__) == False
    print("ready to write to file")

except:
    print("Can't overwrite file. Exiting program.")
    exit

import csv

# The program should then prompt the user for their name, address, and phone number.
__user_name__ = input("Enter Name: ")
__user_address__ = input("Enter Address: ")
__user_phone__ = input("Enter Phone Number: ")
__user_fields__ = ['Name', 'Address', 'Phone']
__user_rows__ = [__user_name__ , __user_address__ , __user_phone__]

# Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user. 
with open(__user_file__, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(__user_fields__) 
        
    # writing the data rows 
    csvwriter.writerow(__user_rows__)

    # Once the data has been written your program should read the file you just wrote to the file system and display the file contents to the user for validation purposes. 
    print("\nSuccess! Wrote the info below.", "\nName: ", __user_name__, "\nAddress", __user_address__, "\nPhone Number", __user_phone__)


# Submit a link to your Github repository.