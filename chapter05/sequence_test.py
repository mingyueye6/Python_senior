# coding: utf-8

from collections import abc

a = [1, 2]
c = a + [3, 4]

# += 就地加
a += [3, 4]

a += 'abc'
print(a)

a.extend(range(3))
print(a)

a.append([1, 2])
print(a)
