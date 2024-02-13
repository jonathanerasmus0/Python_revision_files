class Employee:
    num_of_emps = 0 
    raise_amount = 1.04
    # class variables 
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@hotmail.com"
        
    def full_name(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee("jonathan", "davies", 50000)
emp_2 = Employee("Peter", "davies", 60000)

Employee.set_raise_amt(1.05)


print(Employee.raise_amount)  # Accessing class variable directly
print(emp_1.raise_amount)     # Accessing via instance
print(emp_2.raise_amount)     # Accessing via instance

# Set raise amount using class method
Employee.set_raise_amt(1.05)

print(Employee.raise_amount)  # Accessing class variable after change
print(emp_1.raise_amount)     # Accessing via instance
print(emp_2.raise_amount)     # Accessing via instance


# Static Methods
# behave like regular fuinctions

