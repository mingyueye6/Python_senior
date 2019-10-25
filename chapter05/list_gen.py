# coding: utf-8
# 列表生成式（列表推导式）
# 1. 提取1-20之间的数字

odd_list = []
for i in range(21):
    if i % 2 == 1:
        odd_list.append(i)

odd_list = [i for i in range(21) if i % 2 == 1]

# 2. 逻辑复杂的情况

def hadle_item(item):
    return item* item

odd_list = [hadle_item(i) for i in range(21) if i % 2 == 1]

# 列表生成式性能高于列表操作
print(type(odd_list))
print(odd_list)

# 生成器表达式
odd_list = (i for i in range(21) if i % 2 == 1)
print(type(odd_list))

# 字典推导式
my_dict = {'bobby1': 22, 'bobby2': 23, 'cmooc.com': 5}
reversed_dict = {value:key for key, value in my_dict.items()}
print(reversed_dict)

