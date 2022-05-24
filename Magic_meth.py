class Employee:
    
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullName(self):
        return '{}', '{}'.format(self.first, self.last)
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullName, self.email)

    def __len__(self):
        return len(self.fullName())
        
emp_1 = Employee('Mazhar', 'Naseer', 52000)
emp_2 = Employee('Habib', 'Rafeeq', 60000)

# print(emp_1)

# print(repr(emp_1))          # print(emp_1.__repr__())
# print(str(emp_1))            # print(emp_1.__str__())

print(len(emp_1))


# print(5 + 7)
# print(int.__add__(5, 7))
# print(str.__add__('a', 'b'))