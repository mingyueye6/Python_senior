# coding:utf-8
from collections.abc import Mapping, MutableMapping

a = dict()


# 不建议继承list和dict
from collections import UserDict
# class MyDict(UserDict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value*2)
#
#
# my_dict = MyDict(one=1)
# print(my_dict)

from collections import defaultdict
my_dict = defaultdict(dict())
my_value = my_dict['bobby']
print(my_value)

set()