# Example of a function using *args and **kwargs
def example_function(*args, **kwargs):
    # *args will contain all positional arguments passed to the function
    print("Positional arguments (*args):", args)
    
    # **kwargs will contain all keyword arguments passed to the function
    print("Keyword arguments (**kwargs):", kwargs)

# Call the function with different arguments
example_function(1, 2, 3, name='Jonathan', age=52, city='Berlin')
