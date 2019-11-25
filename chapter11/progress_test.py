# coding: utf-8
# 多进程编程
# 耗CPU的操作，用多进程编程，对于IO操作来说，使用多线程编程，
# 进程切换代价高于线程

# 1.对于耗费CPU的操作，多进程优于多线程
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# if __name__ == "__main__":
#     with ThreadPoolExecutor(3) as executor:
#         all_tack = [executor.submit(fib, (num)) for num in range(25, 35)]
#         start_time = time.time()
#         for future in as_completed(all_tack):
#             data = future.result()
#             print("exe result: {}".format(data))
#         print("last time is:{}".format(time.time() - start_time))
#
#     with ProcessPoolExecutor(3) as executor:
#         all_tack = [executor.submit(fib, (num)) for num in range(25, 35)]
#         start_time = time.time()
#         for future in as_completed(all_tack):
#             data = future.result()
#             print("exe result: {}".format(data))
#         print("last time is:{}".format(time.time() - start_time))

# 2. 对于io操作来说，多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    with ThreadPoolExecutor(3) as executor:
        all_tack = [executor.submit(random_sleep, (num)) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_tack):
            data = future.result()
            print("exe result: {}".format(data))
        print("last time is:{}".format(time.time() - start_time))

    with ProcessPoolExecutor(3) as executor:
        all_tack = [executor.submit(random_sleep, (num)) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_tack):
            data = future.result()
            print("exe result: {}".format(data))
        print("last time is:{}".format(time.time() - start_time))
