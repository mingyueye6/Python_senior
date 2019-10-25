# coding: utf-8
# 上下文管理器协议

class Samle():
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def do_something(self):
        print('doing something')


with Samle() as sample:
    sample.do_something()



