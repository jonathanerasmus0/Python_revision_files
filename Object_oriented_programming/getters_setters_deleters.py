class Employee:
    #initialise or CONSTRUCTOR  Instance variables 
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@hotmail.com"
    def full_name(self):
        return "{} {}".format(self.first, self.last)
    

emp_1 = Employee("jonathan", "davies", 50000)
emp_2 = Employee("Peter", "davies",60000)

print(emp_1.first)
print(emp_1.email)

#corey shafer 
'''@fullname.setter
@fullname.deleter'''
