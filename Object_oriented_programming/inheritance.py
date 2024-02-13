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
    raise_amt = 1.10
    
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp not in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('------>', emp.fullname())
            
    
    
            
        


dev_1 = Developer('jonathan','davies', 50000,'python')
dev_2 = Developer('peter','davies', 600000,'java')

mgr_1 = Manager('Mr BIG', 'BIGGER', 10000000, [dev_1])
print(mgr_1.email)


print(dev_1.email)
print(dev_2.prog_lang)


    

emp_1 = Employee("jonathan", "davies", 50000)
emp_2 = Employee("Peter", "davies",60000)
