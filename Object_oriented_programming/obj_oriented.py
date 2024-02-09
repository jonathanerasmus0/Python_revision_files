# 4 pillars of OOP
#Encapsulation
#abstraction
#Inheritance
#polymorphism

# classes Simple employee Instance variables 
class Employee:
    #initialise or CONSTRUCTOR 
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@hotmail.com"
    def full_name(self):
        return "{} {}".format(self.first, self.last)
    

emp_1 = Employee("jonathan", "davies", 50000)
emp_2 = Employee("Peter", "davies",60000)

'''emp_1.first = "Jonathan"
emp_1.last = "davies"
emp_1.email = "joesaudi@hotmail.com"
emp_1.pay = 50000

emp_2.first = "Peter"
emp_2.last = "davies"
emp_2.email = "joesaudi2@hotmail.com"
emp_2.pay = 60000'''

print(emp_1.email)
print(emp_2.pay)

print ("{} {}".format(emp_1.first, emp_1.last))
print(emp_1.full_name())
print(emp_2.full_name())
    