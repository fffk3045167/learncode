#!/usr/bin/env python
#!-*- coding:utf-8 -*-
#!@Time   : 2020/6/1 21:11
#!@Author : feng
#!File    : tsTclnt3.py

from socket import *


HOST = 'localhost' # or '127.0.0.1'
PORT = 21445
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    # data = str.encode('byte')
    if not data:
        break

    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break

    print(data.decode('utf-8'))

tcpCliSock.close()
