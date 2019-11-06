# coding: utf-8
# gil global interpreter lock
# pyhton 中的一个线程对应于c语言中的一个线程
# gil使同一个时刻只能有一个线程在CPU上执行字节码，无法将多个线程映射到多个CPU上执行

# gil 会根据执行的字节码行数以及时间片释放gil

# import dis
#
# def add(a):
#     a = a + 1
#     return a
#
# print(dis.dis(add))

total = 0

def add():
    global total
    for i in range(100000):
        total += 1

def desc():
    global total
    for i in range(100000):
        total -= 1

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()


print(total)