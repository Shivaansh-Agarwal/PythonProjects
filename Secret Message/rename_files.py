import os
from string import digits

def rename_files():
    # (1)
    # Get all the file names
    # For this we'll use a package named as 'os'
    # In the os package we'll use a function named as listdir()
    file_list = os.listdir(r"E:\B.Tech 3rd Year\Python\Udacity\2. Rename Files in a Directory\prank")
    list_size = len(file_list)
    print("The number of Files in the Directory is: ", list_size)
    for element in file_list:
        print(element)
    # We've used an 'r' before the path because we want to tell Python to take the string as it is
    # and don't interpret any other way.

    # (2)
    # Rename and save them
    # Since an error was coming because the python was not reading in the correct directory
    # I checked the current directory
    saved_path = os.getcwd()
    # print(saved_path)
    # Now for python to work on the files it has to go into that directory
    # Therefore I changed the directory.
    os.chdir(r"E:\B.Tech 3rd Year\Python\Udacity\2. Rename Files in a Directory\prank")

    remove_digits = str.maketrans('', '', digits)
    for file_name in file_list:
        res = file_name.translate(remove_digits)
        print("Old Name: " + file_name)
        print("New name: " + res)
        os.rename(file_name,res)
    os.chdir(saved_path)
    
rename_files()
