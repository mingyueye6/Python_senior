# coding: utf-8
# 事件循环+回调（驱动生成器）+epoll（IO多路复用）
# asyncio是python用于解决异步io编程的一整套解决方案
# tornado，gevent，twisted，(scrapy,django channels)

# import asyncio
# import time
#
# async def get_html(url):
#     print('start get url')
#     await asyncio.sleep(2)
#     print('end get url')
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     tasks = [get_html("http://www.baidu.com")  for i in range(100)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(time.time() - start_time)

# # 获取asyncio的返回值
# import asyncio
# import time
# from functools import partial # 将一个函数包装成另一个函数
#
# async def get_html(url):
#     print('start get url')
#     await asyncio.sleep(2)
#     return "bobby"
#
# def callback(url, future):
#     print('send email to bobby')
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     # get_future = asyncio.ensure_future(get_html("http://www.baidu.com"))
#     task =  loop.create_task(get_html("http://www.baidu.com"))
#     task.add_done_callback(partial(callback, "http://www.baidu.com"))
#     loop.run_until_complete(task)
#     print(task.result())

# wait 和 gather
import asyncio
import time

async def get_html(url):
    print('start get url')
    await asyncio.sleep(2)
    print('end get url')


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # tasks = [get_html("http://www.baidu.com")  for i in range(100)]
    # # loop.run_until_complete(asyncio.wait(tasks))
    # loop.run_until_complete(asyncio.gather(*tasks))
    # print(time.time() - start_time)

    # gather 和 wait 的区别
    group1 = [get_html("http://www.baidu.com") for i in range(2)]
    group2 = [get_html("http://www.baidu.com") for i in range(2)]

    # loop.run_until_complete(asyncio.gather(*group1, *group2))
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    loop.run_until_complete(asyncio.gather(group1, group2))
