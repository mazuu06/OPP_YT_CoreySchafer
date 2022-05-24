class Employee:
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + '.' + lastName + '@company.com'
        self.pay = pay
    
    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)
        

emp_1 = Employee('Naveed', 'Ali', 40000)
emp_2 = Employee('Habib', 'Usman', 50000)



print(emp_1.email)
print(emp_2.email)

print(emp_1.fullName())
print(emp_2.fullName())

print(Employee.fullName(emp_1))