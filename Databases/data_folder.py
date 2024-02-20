import os

# This the folder name where I will store the data. 
folder_name = "data_folder"

# Create the folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created successfully.")

# Define the file path within the folder
file_path = os.path.join(folder_name, "data.txt")

# Sample data to write to the file
data = "bla bla bla bla bla bla bla bla bla bla bla bla"

# Open this file in write mode ("w") with utf-8 encoding
with open(file_path, "w", encoding="utf-8") as file:
    # Write the data to the file
    file.write(data)
    print("Data written to this file has been successful.")

# Open the file in append mode ("a") with utf-8 encoding
with open(file_path, "a", encoding="utf-8") as file:
    # Append additional data to the file
    file.write("\nThis is extra data added or appended to this file.")
    print("Additional data has been added to the file")

# Open the file in read mode ("r") with utf-8 encoding
with open(file_path, "r", encoding="utf-8") as file:
    # Read and print the contents of the file
    file_contents = file.read()
    print("Contents of the file:")
    print(file_contents)


