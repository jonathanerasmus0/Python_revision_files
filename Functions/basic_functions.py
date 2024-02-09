# 1. Defining a basic function
def greet():
    print("Hello, jonathan !")

# 2. Calling a function
greet()

# 3. Function with parameters
def greet_with_name(name):
    print("Hello, " + name + "!")

greet_with_name("Jonathan")

# 4. Function with default parameters
def greet_with_default(name="there"):
    print("Hello, " + name + "!")

greet_with_default()
greet_with_default("Hassan")

# 5. Returning values from a function
def add(a, b):
    return a + b

result = add(3, 5)
print("Result of addition:", result)

# 6. Returning multiple values from a function
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_and_remainder(10, 3)
print("Quotient:", q)
print("Remainder:", r)

# 7. Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# 8. Lambda functions
square = lambda x: x ** 2
print("Square of 4:", square(4))

# 9. Higher-order functions
def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(4, 5, lambda a, b: a + b)
print("Result of addition:", result)

result = apply_operation(4, 5, lambda a, b: a * b)
print("Result of multiplication:", result)

# 10. Nested functions
def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x)

print("Nested function result:", outer_function(5))

# 11. Function annotations (Python 3.x feature)
def annotated_function(x: int, y: int) -> int:
    return x + y

print("Function with annotations:", annotated_function(3, 4))
