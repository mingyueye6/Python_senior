# coding: utf-8
from collections.abc import Iterator

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]


class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            value = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return value



if __name__ == "__main__":
    company = Company(['tome', 'bob', 'jane'])
    my_itor = iter(company)
    with True:
        try:
            print(next(my_itor))
        except StopIteration:
            pass
    for item in company:
        print(item)