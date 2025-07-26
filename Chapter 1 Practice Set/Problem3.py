# Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

# Selet the directory whose content you want to list 
directory_path = '/PYTHON'  
# '.' indicates the current directory

# Use the os module to list the directory content
contents = os.listdir(directory_path)
print("Contents of the directory:")

# Print each file and directory name
for item in contents:
    print(item)