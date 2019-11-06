# coding: utf-8
# 对于io操作来说，多线程和多进程性能差别不大
# 1、通过Thread类实例化
import threading
import time


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(2)
    print("get detail url end")

# 2. 通过集成Thread来实现多线程
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDeatailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(2)
        print("get detail url end")


if __name__ == "__main__":
    # thread1 = threading.Thread(target=get_detail_html, args=("",))
    # thread2 = threading.Thread(target=get_detail_url, args=("", ))
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDeatailUrl("get_detail_url")
    thread1.setDaemon(True)
    thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()

    print("last time:{}".format(time.time() - start_time))
