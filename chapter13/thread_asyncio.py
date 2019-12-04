# coding: utf-8
# 使用多线程：在协程中集成阻塞io
import asyncio
import socket
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

def get_url(url):
    # 通过socket请求URL
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf-8'))

    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf-8')
    html_data = data.split('\r\n\r\n')[1]
    print(html_data)
    client.close()

if __name__ == "__main__":
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    tasks = []
    for i in range(20):
        task = loop.run_in_executor(executor, get_url, "http://www.baidu.com")
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)