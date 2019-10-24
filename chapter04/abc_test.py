# coding: utf-8

# 我们去检查某个类是否有某种方法
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(['bobby1', 'bobby2'])
print(hasattr(com, '__len__'))

# 我们在某些情况之下希望判断某个对象的类型
from collections.abc import Sized
print(isinstance(com, Sized))

# 我们需要强制某个子类必须实现某些方法
# 实现一个web框架，集成cache(redis, cache, memerychache)
# 需要设计一个抽象基类，制定子类必须实现某些方法

# 如何去模拟一个抽象基类
import abc


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

# class CacheBase():
#     def get(self, key):
#         pass

#     def set(self, key, value):
#         pass

#
class RedisCache(CacheBase):
    pass
#
redis_cache = RedisCache()
redis_cache.set('key', 'value')


