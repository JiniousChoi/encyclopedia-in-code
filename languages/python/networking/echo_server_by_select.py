#!/usr/bin/env python2.7
# https://steelkiwi.com/blog/working-tcp-sockets/

from __future__ import print_function
import select, socket, sys, Queue
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('localhost', 50000))
server.listen(5)
inputs = [server]
outputs = []
message_queues = {}

while inputs:
    readable, writable, exceptional = select.select(
        inputs, outputs, inputs)
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print('-- {} : CONNECTED '.format(id(connection)))
            # https://docs.python.org/2/library/socket.html#socket.socket.setblocking
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print('<- {} : {}'.format(id(s), data))
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print('<- {} : {}'.format(id(s), 'FIN'))
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                print('-> {} : {}'.format(id(s), 'ACK+FIN'))
                del message_queues[s]

    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            outputs.remove(s)
        else:
            s.send(next_msg)
            print('-> {} : {}'.format(id(s), next_msg))

    for s in exceptional:
        print('!! {} : {}'.format(id(s), 'exception occured'))
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
