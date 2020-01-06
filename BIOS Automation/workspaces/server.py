#服务器端
# -*- coding:utf-8 -*-

import sys
import socket   #socket模块


local_ip = '15.83.248.221'  # 配置socket server绑定的本地IP
local_port = 54321  # 配置socket server绑定的本地端口


BUF_SIZE = 1024  #设置缓冲区大小
server_address = (local_ip, local_port)  #IP和端口构成表示地址
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #生成一个新的socket对象
print("Socket Created!")
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #设置地址复用
server.bind(server_address)  #绑定地址
print("Socket Bind!")
server.listen(5)  #监听, 最大监听数为5
print("Socket listening")
while True:
    client, client_address = server.accept()  #接收TCP连接, 并返回新的套接字和地址, 阻塞函数
    print('Connected by', client_address)
    while True :
        data = client.recv(BUF_SIZE)  #从客户端接收数据
        print(data)
        client.sendall(data)  #发送数据到客户端
server.close()


