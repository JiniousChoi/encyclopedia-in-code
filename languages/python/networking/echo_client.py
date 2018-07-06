#!/usr/bin/env python3

import socket
import threading as t
from time import sleep

server, port = 'localhost', 50000

def sender_bot(_id):
    msgs = ['hello, I am bot_{x}'.format(x=_id),
            'nice to meet you_{x}'.format(x=_id)]
    def __sender_bot():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
        for msg in msgs:
            sz = s.send(msg.encode())
            print('<- {} : {}'.format(id(s), msg))
            print('-> {} : {}'.format(id(s), s.recv(sz).decode()))
            sleep(1)
        s.close()
    bot_thread = t.Thread(target=__sender_bot)
    bot_thread.start()

bots = 10
for i in range(1, bots+1):
    sender_bot(i)
