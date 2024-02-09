# Example of a set NOTE THE BRACKETS USED 
colors = {'red', 'green', 'blue'}

# Adding elements to a set
colors.add('yellow')

# Removing elements from a set
colors.remove('green')

# Sets automatically remove duplicate elements
colors.add('red')  # This won't add another 'red' since sets only keep unique elements

print("Colors:", colors)

'''Sets are collections of unique elements.
You can add elements to a set using the add() method.
Elements can be removed from a set using the remove() method.
Sets automatically remove duplicate elements, so each element in a set is unique.'''