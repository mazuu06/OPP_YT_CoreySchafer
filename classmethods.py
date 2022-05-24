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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        firstName, lastName, pay = emp_str_1.split('-')
        return cls(firstName, lastName, pay)
        

emp_1 = Employee('Naveed', 'Ali', 40000)
emp_2 = Employee('Habib', 'Usman', 50000)

emp_str_1 = 'Habib-Ali-7000'
emp_str_2 = 'Mudassar-Nafees-9000'
emp_str_3 = 'Hassan-Rafeeq-5000'


new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)


# Employee.set_raise_amt(1.66)
# Employee.raise_amount = 1.6              # This line and above line do same  

# emp_1.set_raise_amt(1.99)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)




