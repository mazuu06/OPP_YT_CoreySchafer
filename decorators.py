from distutils.command.build_scripts import first_line_re


class Employee:
    
    raise_amt = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@yahoo.com'

    @property
    def fullName(self):
        return f'{self.first} {self.last}'

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print("Delete Name!")
        self.first = None
        self.last = None

emp_1 = Employee('Mazhar', 'Naseer')


emp_1.fullName = 'nafees ali'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullName)

del emp_1.fullName
