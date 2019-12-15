#!/usr/bin/env python3
import socket, threading
from queue import Queue
import sys, struct

# NOTE: Use this path to create the UDS Server socket
SERVER_SOCKET_PATH = "./socket";


class Result:
    def __init__(self):
        self._evt = threading.Event()
        self._result = None
    
    def set_result(self, value):
        self._result = value
        self._evt.set()
    
    def result(self):
        self._evt.wait()
        return self._result

class ActorExit(Exception):
    pass

class Actor(object):
    def __init__(self):
        self._mailbox = Queue()
    
    def send(self, msg):
        self._mailbox.put(msg)
        
    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg
    
    def close(self):
        self.send(ActorExit)
        
    def start(self):
        self._terminated = threading.Event()
        t = threading.Thread(target=self._bootstrap)
        t.daemon = True
        t.start()
        
    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()
    
    def join(self):
        self._terminated.wait()
        
    def run(self):
        while True:
            msg = self.recv()
    
class Worker(Actor):
    def __init__(self):
        super().__init__()
        self.db = {}
        
    def submit(self, values):
        r = Result()
        self.send((values, r))
        return r
    
    def run(self):
        while True:
            values, r = self.recv()
            r.set_result(self.execute(values))
    
    def execute(self, values):
        cmd, *opts = values
        print('[*]', cmd, opts)
        if cmd == 1: #add
            s, k, v = opts
            self.db.setdefault(s, {})
            self.db[s][k] = v
            return [0]
        elif cmd == 2: #remove
            s, k = opts
            if s in self.db and k in self.db[s]:
                self.db[s].pop(k)
            return [0]
        elif cmd == 3: #get size
            s = opts[0]
            size = len(self.db[s]) if s in self.db else 0
            return [1, size]
        elif cmd == 4: #get value
            s, k = opts
            if s in self.db and k in self.db[s]:
                score = self.db[s][k]
            else:
                score = 0
            return [1, score]
        elif cmd == 5: #range
            *sets, _, lower, upper = opts
            res = []
            for s in sets:
                if s not in self.db:
                    continue
                for k,v in self.db[s].items():
                    if lower <= v <= upper:
                        res.append((k,v))
            res.sort()
            return [len(res)*2] + [e for kv in res for e in kv]
        elif cmd == 6: #disconnect
            return None
        else:
            raise Exception("Not supported CMD(%s)" % (cmd))


FMT = "!L"

def read_number_from_socket(connection):
    return struct.unpack(FMT, connection.recv(4))[0]

def write_number_to_socket(connection, number):
    connection.send(struct.pack(FMT, number))
    
def process_client_connection(connection, worker):
    while True:
        value_num = read_number_from_socket(connection)
        
        values = []
        for _ in range(value_num):
            values.append(read_number_from_socket(connection))
            
        res = worker.submit(values)
        if res.result() == None:
            break
            
        for num in res.result():
            write_number_to_socket(connection, num)
        
    connection.close()

def main():
    worker = Worker()
    worker.start()
    
    s = socket.socket(socket.AF_UNIX)
    s.bind(SERVER_SOCKET_PATH)
    s.listen(1)
    while True:
        cl, addr = s.accept()
        t = threading.Thread(target = process_client_connection, args=(cl, worker))
        t.start()
        
    #worker.close()
    s.close()

if __name__ == '__main__':
    main()
