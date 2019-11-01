# coding: utf-8
# __getattr__ 就是在查找不到属性的时候调用
# __getattribute__
from datetime import date


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __getattr__(self, item):
        print(('not find attr'))


if __name__ == "__main__":
    user = User('bobby', date(year=1987, month=1, day=1))
    print(user.age)
