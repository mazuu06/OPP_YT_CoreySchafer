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
        firstName, lastName, pay = emp_str.split('-')
        return cls(firstName, lastName, pay)
    
    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Naveed', 'Ali', 40000)
emp_2 = Employee('Habib', 'Usman', 50000)

import datetime
my_date = datetime.date(2046, 8, 15)
print(Employee.is_working(my_date))
