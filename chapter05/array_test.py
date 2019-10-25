# coding: utf-8
# array(数组), deque

import array
# array和list的重要区别，array只能存放指定的数据类型
my_array = array.array('i')

my_array.append(1)
my_array.append(2)
# my_array.append(['abc'])
print(my_array)
