# coding: utf-8
# 生成器函数，函数里只要有yield关键字


def gen_func():
    yield 1
    yield 2
    yield 3


# 惰性求值，延迟求值
def fib(index):
    if index == 0:
        return 0
    elif index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


# print(fib(5))

def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1

for data in gen_fib(10):
    print(data)




def func():
    return 1


if __name__ == "__main__":
    gen = gen_func()
    re = func()
    pass
