#客户端
# -*- coding:utf-8 -*-

import socket

server_ip = "15.83.248.221"
server_port = "54321"

BUF_SIZE = 1024  #设置缓冲区的大小
server_address = (server_ip, server_port)  #IP和端口构成表示地址
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #返回新的socket对象
client.connect(server_address)  #要连接的服务器地址
while True:
    data = raw_input("Please input some string > ")  
    client.sendall(data)  #发送数据到服务器
    data = client.recv(BUF_SIZE)  #从服务器端接收数据
    print(data)
client.close()
