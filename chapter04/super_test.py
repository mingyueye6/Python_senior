# coding: utf-8

class A:
    def __init__(self):
        print('a')


class B(A):
    def __init__(self):
        print('b')
        super().__init__()


from threading import Thread
class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        super().__init__(name=name)

if __name__ == '__main__':
    b = B()


# mixin模式
#     1、mixin类功能单一
#     2、不和基类关联，可以和任意基类组合，基类可以不和mixin关联就能初始化成功
#     3、在mixin中不要使用super这种用法
