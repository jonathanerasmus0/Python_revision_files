class Employee:
    
    raise_amount = 1.04
    #class variables 
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@hotmail.com"
    def full_name(self):
        return "{} {}".format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
    
emp_1 = Employee("jonathan", "davies", 50000)
emp_2 = Employee("Peter", "davies",60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_2.pay)

#end
