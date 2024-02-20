'''Exercise 03: How to create and store json object to a file

Create a variable called student_data which will hold a dictionary with a name and role like this: student_data = { "name": "Arif", "role": "teacher" }
Convert this dictionary to a JSON string using the dumps() method from the json module.
Save the output in to a JSON file (with an extension: example.json).'''

import json

# Create a dictionary to hold student data
student_data = {
    "name": "Arif",
    "role": "teacher"
}

# Convert the dictionary to a JSON string
json_string = json.dumps(student_data, indent=4)

# Specify the file path where the JSON file will be saved
file_path = "example.json"

# Write the JSON string to the file
with open(file_path, 'w') as json_file:
    json_file.write(json_string)

print(f"JSON data has been successfully saved to '{file_path}'")

'''PERSONAL EXPLANATION TO HELP WITH FUTURE REVISION: The selected code is a Python script that demonstrates how to convert a Python dictionary to a JSON string and save it to a file.

The script starts by creating a dictionary called student_data that contains two key-value pairs: name and role.

Then, it uses the json.dumps() function to convert the dictionary to a JSON string, with an indentation of 4 spaces.

Next, the script specifies the file path where the JSON file will be saved (in this case, example.json).

Finally, the script uses the with open() as json_file: syntax to open a file with the specified file path, write the JSON string to the file, and close the file.

The script then prints a message to the console indicating that the JSON data has been successfully saved to the specified file path.

Overall, the selected code demonstrates how to convert a Python dictionary to a JSON string and save it to a file, which can be useful for storing and transferring data in a structured and readable format. '''