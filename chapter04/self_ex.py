# coding: utf-8
# python的自省机制
from chapter04.class_method import Date
class Person:
    name = 'user'

class Student(Person):
    def __init__(self, school_name):
        self.scool_name = school_name



if __name__ == '__main__':
    user = Student('慕课网')

    # 通过__dict__查询属性
    print(user.__dict__)
    print(Person.__dict__)
    print(user.name)