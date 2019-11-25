# coding: utf-8
# multiprocessing 多线程编程
import os
import time

# fork  只能用于Linux/Unix中

# pid = os.fork()
# print("bobby")
# if pid == 0:
#     print("子进程 {}，父进程 {}".format(os.getgid(), os.getppid()))
# else:
#     print("我是父进程 {}".format(pid))
#
# time.sleep(2)

import multiprocessing

# 多进程编程
import time

def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n

if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3,))

    # 等待任务完成
    # pool.close()
    # pool.join()
    # print(result.get())

    # imap
    for result in pool.imap(get_html, [1, 5, 3]):
        print("{} sleep success".format(result))

