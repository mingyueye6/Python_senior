# coding: utf-8

import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen()

def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        re_data = input('请输入:')
        sock.send(re_data.encode('utf-8'))

# 获取从客户端发送的数据
while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

# server.close()
# sock.close()