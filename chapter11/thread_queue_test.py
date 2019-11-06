# coding: utf-8
# 通过queue的方式进行线程间通信

import threading
import time
from queue import Queue


def get_detail_html(queue):
    # 抓取文章详情页
    while True:
        url = queue.get()
        # for url in detail_url_list:
        print("get detail html started")
        time.sleep(4)
        print("get detail html end")


def get_detail_url(queue):
    # 抓取文章列表页
    print("get detail url started")
    while True:
        time.sleep(4)
        for i in range(20):
            queue.put("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")


# 1、线程间的通信方式 - 共享变量


if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()
    thread_detail_url.start()

    detail_url_queue.task_done()
    detail_url_queue.join()