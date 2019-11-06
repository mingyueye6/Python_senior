# coding: utf-8

from concurrent.futures import ThreadPoolExecutor

# 线程池
# 主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
# 当一个线程完成的时候我们主线程能立即知道
# futures可以让多线程和多进程编码接口一致

import time

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))

executor = ThreadPoolExecutor(max_workers=2)
# 通过sumbit函数提交执行的函数到线程池中
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (2))

# done 方法用户判断某个任务是否完成
print(task1.done())
# print(task2.cancel()) # 可以取消未进入线程池的线程
time.sleep(5)
print(task1.done())

# result方法可以获取task的执行结果
print(task1.result())


if __name__ == '__main__':
    print(11111)