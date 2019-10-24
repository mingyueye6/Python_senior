# coding: utf-8
# C3算法

class D:  # 新式类
    pass

class E(object):
    pass

class C(E):
    pass

class B(D):
    pass

class A(B,C):
    name = 'A'
    def __init__(self):
        self.name = 'obj'


print(A.__mro__)
a = A()
print(a.name)

