# coding: utf-8
# 用来处理已排序的序列，用来维持已排序的序列

import bisect

inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 4)
print(inter_list)

print(bisect.bisect(inter_list, 3))