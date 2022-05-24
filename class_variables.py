class Employee:
    num_of_emp = 125
    raise_amount = 1.04
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + '.' + lastName + '@company.com'
        self.pay = pay
        Employee.num_of_emp += 1
        
    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)
     
    def apply_raise(self):
           self.pay = int(self.pay * self.raise_amount)
           print(self.num_of_emp)

print(Employee.num_of_emp)
emp_1 = Employee('Naveed', 'Ali', 40000)
emp_2 = Employee('Habib', 'Usman', 50000)


# print(emp_1.__dict__)
# print("*****************************")
# print(Employee.__dict__)

# Employee.raise_amount = 15
emp_1.raise_amount = 1.55

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

print(Employee.num_of_emp)
emp_2.apply_raise()

 #Employee.apply_raise(self)


