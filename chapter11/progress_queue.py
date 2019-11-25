# coding: utf-8
# 进程间通信
import time
from multiprocessing import Process, Queue, Pool, Manager, Pipe

# def producer(queue):
#     queue.put('a')
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
# if __name__ == "__main__":
#     queue = Queue(10)
#     my_producer = Process(target=producer, args=(queue,))
#     my_consumer = Process(target=consumer, args=(queue,))
#     my_producer.start()
#     my_consumer.start()
#
#     my_producer.join()
#     my_consumer.join()

# multiprocessing中的queue不能用于进程池中
# pool中的进程间通信需要使用manager中的queue

# def producer(queue):
#     queue.put('a')
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
#
# if __name__ == "__main__":
#     queue = Manager().Queue(10)
#     pool = Pool(2)
#     pool.apply_async(producer, args=(queue, ))
#     pool.apply_async(consumer, args=(queue,))
#
#     pool.close()
#     pool.join()

# 通过pipe实现进程间通信

# def producer(pipe):
#     pipe.send('a')
#
#
# def consumer(pipe):
#     print(pipe.recv())
#
#
# if __name__ == "__main__":
#     receive_pipe, send_pipe = Pipe()
#     # pipe只能适用于两个进程
#     my_producer = Process(target=producer, args=(send_pipe,))
#     my_consumer = Process(target=consumer, args=(receive_pipe,))
#     my_producer.start()
#     my_consumer.start()
#
#     my_producer.join()
#     my_consumer.join()

# 共享变量

def add_data(p_dict, key, value):
    p_dict[key] = value

if __name__ == "__main__":
    process_dic = Manager().dict()

    first_progress = Process(target=add_data, args=(process_dic, 'bobby1', 21))
    second_progress = Process(target=add_data, args=(process_dic, 'bobby2', 22))
    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()
    print(process_dic)