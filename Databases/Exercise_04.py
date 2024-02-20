'''Exercise 04: How to Read json data

Open the existing json data file in the read mode (r).

Print the data to the screen.

Your result may be look like the result below:

{"name": "arif", "role": "teacher"}'''

import json

# Specify the file path of the JSON file
file_path = "example.json"

# Open the JSON file in read mode
with open(file_path, 'r') as json_file:
    # Load the JSON data from the file
    json_data = json.load(json_file)

# Print the JSON data to the screen
print(json_data)
