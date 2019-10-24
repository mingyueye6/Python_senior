# coding: utf-8
# type,object,class的关系

print(type(1))
print(type(int))

print(type('asd'))
print(type(str))

# type-->int-->1

# object 是最顶层基类
# type 也是一个类，同时type也是一个对象

class Student:
    pass

stu = Student()
print(type(stu))
print(type(Student))
print(int.__bases__)
print(str.__bases__)



class MyStudent(Student):
    pass

stu = MyStudent()
print(type(stu))
print(type(MyStudent))
print(type.__bases__)
print(object.__bases__)
print(type(object))


