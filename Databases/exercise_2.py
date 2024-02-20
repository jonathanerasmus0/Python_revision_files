'''Exercise 02: How read data from File-System disk/your computer

Read the contents of the file provided in data.txt. Print the results in your terminal using Python. The mode="r" can be used when reading the file.'''



# Full path to the file
file_path = '/Users/jonathanerasmusdavies/PYTHON/Python_revision_files_02/Python_revision_files/Databases/data.txt'

# Open the file in read mode
with open(file_path, mode='r') as file:
    # Read the contents of the file
    file_contents = file.read()

# Print the contents to the terminal
print(file_contents)

