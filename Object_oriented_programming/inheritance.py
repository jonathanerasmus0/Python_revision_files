class Employee:
    raise_amt = 1.04
    #initialise or CONSTRUCTOR  Instance variables 
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@hotmail.com"
    def full_name(self):
        return "{} {}".format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee): # developer class is now inheriting from Employee class
    pass

dev_1 = Developer('jonathan','davies', 50000)
dev_2 = Developer('peter','davies', 600000)

print(dev_1.email)

    

emp_1 = Employee("jonathan", "davies", 50000)
emp_2 = Employee("Peter", "davies",60000)
