# coding: utf-8
# 对于io操作来说，多线程和多进程性能差别不大
# 1、通过Thread类实例化
import threading
import time

from chapter11 import variables


def get_detail_html():
    # 抓取文章详情页
    detail_url_list = variables.detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            # for url in detail_url_list:
            print("get detail html started")
            time.sleep(4)
            print("get detail html end")


def get_detail_url():
    # 抓取文章列表页
    print("get detail url started")
    detail_url_list = variables.detail_url_list
    while True:
        time.sleep(2)
        for i in range(20):
            detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
        print("get detail url end")


# 1、线程间的通信方式 - 共享变量


if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_detail_url)
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html)
        html_thread.start()
    thread_detail_url.start()

