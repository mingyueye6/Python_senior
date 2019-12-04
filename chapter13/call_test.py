# coding: utf-8
import asyncio

def callback(sleep_times, loop):
    # print("sleep {}s".format(sleep_times))
    print("sleep {}s".format(loop.time()))

def stoploop(loop):
    loop.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    now = loop.time()
    # loop.call_at(now + 2, callback, loop)
    # loop.call_later(1, callback, 1)
    # loop.call_soon(callback, 2)
    loop.call_soon(callback, 4, loop)
    # loop.call_soon(stoploop, loop)
    loop.run_forever()