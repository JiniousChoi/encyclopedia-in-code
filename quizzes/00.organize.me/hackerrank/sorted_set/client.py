#!/usr/bin/env python3

import socket
import struct
import threading

SERVER_SOCKET_PATH = "./socket"

FMT = "!L"

def read_number_from_socket(connection):
    return struct.unpack(FMT, connection.recv(4))[0]

def write_number_to_socket(connection, number):
    connection.send(struct.pack(FMT, number))

def client(t_id):
    sock = socket.socket(socket.AF_UNIX)
    sock.connect(SERVER_SOCKET_PATH)

    with open('./input.txt', 'r') as fp:
        commands = fp.read()

    for command in commands.splitlines():
        for opt in command.split():
            sock.send(struct.pack(FMT, int(opt)))
        value_cnt = read_number_from_socket(sock)
        print(value_cnt)
        for _ in range(value_cnt):
            value = read_number_from_socket(sock)
            #print('tid', t_id, value)
            print(value)
    sock.close()
    print('termnated', t_id)


def main():
    for t_id in range(1):
        t = threading.Thread(target=client, args=(t_id,))
        t.start()

if __name__ == "__main__":
    main()
