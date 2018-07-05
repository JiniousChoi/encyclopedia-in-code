# echo_server_by_select
```console
$ ./echo_server_by_select.py 
-- 4391975744 : CONNECTED 
-- 4391975968 : CONNECTED 
<- 4391975744 : hello, I am bot_5
-- 4391976416 : CONNECTED 
-> 4391975744 : hello, I am bot_5
-- 4391976192 : CONNECTED 
<- 4391976416 : hello, I am bot_7
-- 4391976752 : CONNECTED 
<- 4391976192 : hello, I am bot_10
-> 4391976416 : hello, I am bot_7
<- 4391975968 : hello, I am bot_8
<- 4391976752 : hello, I am bot_2
-> 4391976192 : hello, I am bot_10
-> 4391975968 : hello, I am bot_8
-> 4391976752 : hello, I am bot_2
<- 4391975744 : nice to meet you_5
<- 4391975968 : nice to meet you_8
<- 4391976192 : nice to meet you_10
<- 4391976752 : nice to meet you_2
-> 4391975744 : nice to meet you_5
<- 4391976416 : nice to meet you_7
-> 4391975968 : nice to meet you_8
-> 4391976192 : nice to meet you_10
-> 4391976752 : nice to meet you_2
-> 4391976416 : nice to meet you_7
<- 4391976752 : FIN
-> 4391976752 : ACK+FIN
<- 4391975744 : FIN
-> 4391975744 : ACK+FIN
<- 4391975968 : FIN
-> 4391975968 : ACK+FIN
<- 4391976192 : FIN
-> 4391976192 : ACK+FIN
<- 4391976416 : FIN
-> 4391976416 : ACK+FIN
```

# echo_client
ConnectionResetError occurs because the server listens only up to 5 clients
```console
$ ./echo_client.py 
-> 4552850408 : hello, I am bot_5
-> 4552850984 : hello, I am bot_10
-> 4552850696 : hello, I am bot_7
-> 4552380136 : hello, I am bot_2
-> 4552850792 : hello, I am bot_8
Exception in thread Thread-4:
Traceback (most recent call last):
  File "/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "./echo_client.py", line 17, in __sender_bot
    print('-> {} : {}'.format(id(s), s.recv(sz).decode()))
ConnectionResetError: [Errno 54] Connection reset by peer

Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "./echo_client.py", line 17, in __sender_bot
    print('-> {} : {}'.format(id(s), s.recv(sz).decode()))
ConnectionResetError: [Errno 54] Connection reset by peer
Exception in thread Thread-3:
Traceback (most recent call last):
  File "/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "./echo_client.py", line 17, in __sender_bot
    print('-> {} : {}'.format(id(s), s.recv(sz).decode()))
ConnectionResetError: [Errno 54] Connection reset by peer

Exception in thread Thread-9:
Traceback (most recent call last):
  File "/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "./echo_client.py", line 17, in __sender_bot
    print('-> {} : {}'.format(id(s), s.recv(sz).decode()))
ConnectionResetError: [Errno 54] Connection reset by peer

Exception in thread Thread-6:
Traceback (most recent call last):
  File "/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "./echo_client.py", line 17, in __sender_bot
    print('-> {} : {}'.format(id(s), s.recv(sz).decode()))
ConnectionResetError: [Errno 54] Connection reset by peer


-> 4552850408 : nice to meet you_5
-> 4552850792 : nice to meet you_8
-> 4552380136 : nice to meet you_2
-> 4552850984 : nice to meet you_10
-> 4552850696 : nice to meet you_7
```
