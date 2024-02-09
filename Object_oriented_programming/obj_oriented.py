# 4 pillars of OOP
#Encapsulation
#abstraction
#Inheritance
#polymorphism

# classes Simple employee 
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "hotmail.com"
    def fullname

emp_1 = Employee("jonathan", "davies", 50000)
emp_2 = Employee()

emp_1.first = "Jonathan"
emp_1.last = "davies"
emp_1.email = "joesaudi@hotmail.com"
emp_1.pay = 50000

emp_2.first = "Jonathan"
emp_2.last = "davies"
emp_2.email = "joesaudi@hotmail.com"
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.pay)


    