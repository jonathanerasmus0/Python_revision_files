# double underscore is often referred to as dunder
# this fucntion is usually used for developers
class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@hotmail.com"
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    def __repr__(self): #used for developers to see
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    def __add__(self,other):
        return self.pay+other.pay
    
    

emp_1 = Employee('jonathan', 'davies', 50000)
emp_2 = Employee('peter', 'davies', 60000)

print(len("peter"))
print('peter'.__len__())
print(len(emp_1))



print(emp_1)
print(emp_2)

#special methods for maths
print(1+2)
print(int.__add__(1,2))
print(str.__add__('a','b')) # you can only xconcatenate 2 strings

# add two employees togethr

print(emp_1 + emp_2)

