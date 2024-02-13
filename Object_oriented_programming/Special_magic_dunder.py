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

emp_1 = Employee('jonathan', 'davies', 50000)
emp_2 = Employee('peter', 'davies', 60000)

print(emp_1)
