'''def greet():
    print("hi there")
    print("welcome")
    
greet()'''


#adding parameters
def greet(first_name, last_name):
    print(f"hi{first_name}{last_name}")
    print("welcome")
    
greet("jonatan", "davies")

#types of functions
#1 Perform a task
# return a value

def get_greeting(name):
    return (f"Hi {name}")
    

message = get_greeting("jon")

def increment(number, by):
    return number + by

result = increment(2,1)
print(result)

#default 
def increment(number, by):
    return number + by


def increment(number, by=1):
    return number + 1


print(increment(2, 5))

#args
def multiply(x, y):
    return x * y

answer = multiply(2,3)
print(answer)

#arges
def multiply(*numbers):
    print(numbers)

multiply(2,3,4,5,6)

# iterate

'''def multiply(*numbers):
    total = 1
    for number in numbers:
        

multiply(2,3,4,5,6)'''
#dictionary function 
def save_user(**user):
    print(user)
    

save_user(id=1, name="jon", age=22)

#scope local variables 
def greet(name):
    message = "a"
    
def send_email(name):
    message = "b"
    

greet("jon")


