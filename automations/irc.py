#!/usr/bin/env python3

import socket

DEBUG = False
server = "chat.freenode.net"
username = "jinchoi"
hostname = 'tolmoon'
servername = 'tolsun'
realname = 'jinchoi'
channel = "#jinchoi" 

def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, 6667))
    return sock

def send(conn, msg):
    conn.send(msg.encode())

def sendmsg(conn, msg):
    send(conn, "PRIVMSG "+ channel +" :"+ msg +"\n")

def block(conn):
    while True:
        data = conn.recv(1024)
        if DEBUG:
            print(data.decode(), end='')
        if not data:
            break

def quit(conn):
    send(conn, "QUIT\n")

def main(args):
    conn = connect()
    send(conn, "USER "+ username +" "+ hostname +" "+ servername + " " + realname + "\n") # user authentication
    send(conn, "NICK "+ username +"\n") # assign the nick to the bot
    send(conn, "JOIN "+ channel +"\n")
    sendmsg(conn, args.data)
    quit(conn)
    block(conn)
    conn.close()

def args_maker(msg):
    from collections import namedtuple
    Args = namedtuple('Args', 'data')
    args = Args(msg)
    return args

if __name__ == "__main__":
    args = args_maker("Mayday, mayday!")
    main(args)
