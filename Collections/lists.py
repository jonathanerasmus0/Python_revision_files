# Example of a list
fruits = ['apple', 'banana', 'orange', 'grape']

# Accessing elements in a list
print("First fruit:", fruits[0])  # Indexing starts from 0 DONT FORGET THIS

# Adding elements to a list using APPEND TO ADD 
fruits.append('kiwi')  # Add 'kiwi' to the end of the list
print("Fruits after adding 'kiwi':", fruits)

# Removing elements from a list USING POP
removed_fruit = fruits.pop(2)  # Remove the fruit at index 2 (orange)
print("Removed fruit:", removed_fruit)
print("Fruits after removing 'orange':", fruits)

'''Lists are like containers where you can keep multiple items together.
You can access elements in a list using their index (position in the list).
Elements can be added to the end of a list using the append() method.
Elements can be removed from a list using the pop() method by specifying the index of the element to be removed.'''