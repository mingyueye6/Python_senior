# coding: utf-8

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def __str__(self):
        return ','.join(self.employee)

    def __repr__(self):
        return ','.join(self.employee)


company = Company(['tome', 'bob', 'jane'])
print(company)
# company
# emploee = company.employee
# for em in company:
#     print(em)
class Nums(object):
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)


my_num = Nums(1)
abs(my_num)

set()

