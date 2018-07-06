# 5 bots from client
```console
$ ./echo_server_by_select.py            $ ./echo_client.py 
-- 4340103776 : CONNECTED               <- 4303214152 : hello, I am bot_4
-- 4340104000 : CONNECTED               <- 4302742824 : hello, I am bot_1
<- 4340103776 : hello, I am bot_1       <- 4302745320 : hello, I am bot_2
-- 4340104224 : CONNECTED               <- 4303213288 : hello, I am bot_3
<- 4340104000 : hello, I am bot_2       <- 4303215592 : hello, I am bot_5
-> 4340103776 : hello, I am bot_1       -> 4302742824 : hello, I am bot_1
-- 4340104448 : CONNECTED               -> 4302745320 : hello, I am bot_2
<- 4340104224 : hello, I am bot_3       -> 4303213288 : hello, I am bot_3
-> 4340104000 : hello, I am bot_2       -> 4303214152 : hello, I am bot_4
-- 4340104672 : CONNECTED               -> 4303215592 : hello, I am bot_5
<- 4340104448 : hello, I am bot_4       <- 4302742824 : nice to meet you_1
-> 4340104224 : hello, I am bot_3       <- 4303215592 : nice to meet you_5
<- 4340104672 : hello, I am bot_5       <- 4303214152 : nice to meet you_4
-> 4340104448 : hello, I am bot_4       <- 4303213288 : nice to meet you_3
-> 4340104672 : hello, I am bot_5       <- 4302745320 : nice to meet you_2
<- 4340103776 : nice to meet you_1      -> 4302742824 : nice to meet you_1
<- 4340104000 : nice to meet you_2      -> 4302745320 : nice to meet you_2
<- 4340104224 : nice to meet you_3      -> 4303213288 : nice to meet you_3
<- 4340104672 : nice to meet you_5      -> 4303215592 : nice to meet you_5
-> 4340103776 : nice to meet you_1      -> 4303214152 : nice to meet you_4
<- 4340104448 : nice to meet you_4      
-> 4340104000 : nice to meet you_2      
-> 4340104224 : nice to meet you_3      
-> 4340104672 : nice to meet you_5      
-> 4340104448 : nice to meet you_4      
<- 4340103776 : FIN 
-> 4340103776 : ACK+FIN                 
<- 4340104000 : FIN 
-> 4340104000 : ACK+FIN                 
<- 4340104224 : FIN 
-> 4340104224 : ACK+FIN                 
<- 4340104448 : FIN 
-> 4340104448 : ACK+FIN                 
<- 4340104672 : FIN 
-> 4340104672 : ACK+FIN
```

# 10 bots from client
```console
$ ./echo_server_by_select.py            $ ./echo_client.py 
-- 4549544544 : CONNECTED               <- 4471419624 : hello, I am bot_3
-- 4549544768 : CONNECTED               <- 4470945064 : hello, I am bot_1
-- 4549544992 : CONNECTED               <- 4470947560 : hello, I am bot_2
<- 4549544544 : hello, I am bot_7       <- 4471422408 : hello, I am bot_9
-- 4549545216 : CONNECTED               <- 4471422120 : hello, I am bot_6
<- 4549544992 : hello, I am bot_5       <- 4471422504 : hello, I am bot_10
-> 4549544544 : hello, I am bot_7       <- 4471422216 : hello, I am bot_7
-- 4549545440 : CONNECTED               <- 4471421928 : hello, I am bot_5
<- 4549545216 : hello, I am bot_4       <- 4471422312 : hello, I am bot_8
-> 4549544992 : hello, I am bot_5       <- 4471420488 : hello, I am bot_4
<- 4549544768 : hello, I am bot_8       Exception in thread Thread-9:
<- 4549545440 : hello, I am bot_10      ConnectionResetError: [Errno 54] Connection reset by peer
-> 4549545216 : hello, I am bot_4       -> 4471422504 : hello, I am bot_10
-> 4549544768 : hello, I am bot_8       -> 4471422216 : hello, I am bot_7
-> 4549545440 : hello, I am bot_10      -> 4471421928 : hello, I am bot_5
<- 4549544992 : nice to meet you_5      -> 4471422312 : hello, I am bot_8
<- 4549545440 : nice to meet you_10     Exception in thread Thread-1:
<- 4549545216 : nice to meet you_4      ConnectionResetError: [Errno 54] Connection reset by peer
-> 4549544992 : nice to meet you_5      -> 4471420488 : hello, I am bot_4
-> 4549545440 : nice to meet you_10     Exception in thread Thread-3:
<- 4549544544 : nice to meet you_7      ConnectionResetError: [Errno 54] Connection reset by peer
<- 4549544768 : nice to meet you_8      Exception in thread Thread-2:
-> 4549545216 : nice to meet you_4      ConnectionResetError: [Errno 54] Connection reset by peer
-> 4549544544 : nice to meet you_7      Exception in thread Thread-6:
-> 4549544768 : nice to meet you_8      ConnectionResetError: [Errno 54] Connection reset by peer
<- 4549544544 : FIN                     <- 4471422504 : nice to meet you_10
-> 4549544544 : ACK+FIN                 <- 4471420488 : nice to meet you_4
<- 4549545216 : FIN                     <- 4471421928 : nice to meet you_5
-> 4549545216 : ACK+FIN                 <- 4471422216 : nice to meet you_7
<- 4549545440 : FIN                     <- 4471422312 : nice to meet you_8
-> 4549545440 : ACK+FIN                 -> 4471421928 : nice to meet you_5
<- 4549544768 : FIN                     -> 4471422504 : nice to meet you_10
-> 4549544768 : ACK+FIN                 -> 4471420488 : nice to meet you_4
<- 4549544992 : FIN                     -> 4471422216 : nice to meet you_7
-> 4549544992 : ACK+FIN                 -> 4471422312 : nice to meet you_8
```
