# coding: utf-8

a = 1
# 1. a贴在1上面
# 2. 先生成对象，然后贴便利贴
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(a is b)

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print(a is b)
