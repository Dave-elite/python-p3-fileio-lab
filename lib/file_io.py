# Lets practice! In the file lib/file_io.py write a function called write_file that takes in the arguments file_name and file_content.

# The file_name can be a combined file path/name, you will need to add the .txt file extension to the file_name when opening a file for all three of the methods.

# This function should use file_name and file_content to write a .txt file.

# Write a append_file function that takes in the same parameters and appends to the .txt file.

# Write a read_file function that takes in a file name and returns the content of the .txt file.

# Example usage:

# # use write_file function. 
# write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
# append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

# read_file(file_name="logfile")
# # Log 1: 5 bananas added
# # Log 2: 3 bananas subtracted
# Time to get some practice! Write your code in the file_io.py file in the lib/ folder. Run pytest -x to check your work.

# When all of your tests are passing, submit your work using git.


def write_file(file_name = "logfile", file_content = "Log 1: 5 bananas added\n"):
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, 'w') as file:
        file.write(file_content)
    pass

def append_file(file_name, append_content):
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, 'a') as file:
        file.write(append_content)
    pass

def read_file(file_name):
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, 'r') as file:
        return file.read()  # returns the content of the file as a string.
    pass
