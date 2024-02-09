# Example of a dictionary
student = {'name': 'Jonathan', 'age': 52, 'grade': '12th'}

# Accessing values in a dictionary using keys
print("Name:", student['name'])
print("Age:", student['age'])
print("Grade:", student['grade'])

# Adding new key-value pairs to a dictionary
student['city'] = 'New York'

# Modifying values in a dictionary
student['age'] = 13

# Removing key-value pairs from a dictionary
del student['grade']

print("Student details:", student)

'''Dictionaries are like real-life dictionaries where you look up a word (key) to find its meaning (value).
Each item in a dictionary consists of a key and its corresponding value.
You can access values in a dictionary using their keys.
New key-value pairs can be added to a dictionary, existing values can be modified, and key-value pairs can be removed using the del keyword.'''
