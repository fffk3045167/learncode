#!/usr/bin/env python
#!-*- coding:utf-8 -*-
#!@Time   : 2020/5/31 22:16
#!@Author : feng
#!File    : tsTserv3.py

from socket import *
from time import ctime


HOST = ''
PORT = 21345
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from: ', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[{}]{}'.format(bytes(ctime(), 'utf-8'), data))

    tcpCliSock.close()

tcpSerSock.close()