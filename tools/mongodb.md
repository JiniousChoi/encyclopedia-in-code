# [MongDB Tutorial](https://www.youtube.com/playlist?list=PLC3y8-rFHvwh11bWtwm3_qKvo46uDmaal) demo via docker containers

## [terminal 1] Run `mongod`
```
$ docker run --rm --name mongo34 mongo:3.4
2018-08-17T00:24:10.533+0000 I CONTROL  [initandlisten] MongoDB starting : pid=1 port=27017 dbpath=/data/db 64-bit host=74717207add3
2018-08-17T00:24:10.533+0000 I CONTROL  [initandlisten] db version v3.4.16
2018-08-17T00:24:10.533+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.1t  3 May 2016
...
2018-08-17T00:24:10.676+0000 I NETWORK  [thread1] waiting for connections on port 27017
```

## [terminal 2] Connect to `mongod` via `mongo` shell
```
$ docker run --rm -it mongo:3.4 bash
root@e2c5b75cca48:/# mongo 172.17.0.13 # got the ip address using `docker inspect mongo34`
MongoDB shell version v3.4.16
connecting to: mongodb://172.17.0.13:27017/test
MongoDB server version: 3.4.16
Welcome to the MongoDB shell.
...

> db
test
```

## [terminal 1] `mongod` accepted connection
```
2018-08-17T00:35:34.940+0000 I NETWORK  [thread1] connection accepted from 172.17.0.14:50870 #1 (1 connection now open)
2018-08-17T00:35:34.941+0000 I NETWORK  [conn1] received client metadata from 172.17.0.14:50870 conn1: { application: { name: "MongoDB Shell" }, driver: { name: "MongoDB Internal Client", version: "3.4.16" }, os: { type: "Linux", name: "PRETTY_NAME="Debian GNU/Linux 8 (jessie)"", architecture: "x86_64", version: "Kernel 4.9.93-linuxkit-aufs" } }
```

## [terminal 2] Create db -> collection -> document in `mongo`
```
> show dbs
admin  0.000GB
local  0.000GB

> db
test

> use testdb
switched to db testdb

> show dbs  // testdb will be initialized once a document is inserted
admin  0.000GB
local  0.000GB

> db.testcollection.insert({"name":"jin.c"})
WriteResult({ "nInserted" : 1 })

> show dbs  // now it's created. When all collections are delete, the db will be gone, too
admin   0.000GB
local   0.000GB
testdb  0.000GB

> db.testcollection.find()
{ "_id" : ObjectId("5b76346072d49ab6027b1ff2"), "name" : "jin.c" }
```
