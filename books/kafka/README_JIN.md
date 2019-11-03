# Exercise for Ch02

```
docker-compose up -d
```

```
kafka-topics.sh --zookeeper zookeeper1:2181,zookeeper2:2181,zookeeper3:2181 --replication-factor=1 --partitions 1 --topic jin-topic --create
```

```
nc -v zookeeper1 2181
nc -v zookeeper2 2181
nc -v zookeeper3 2181
```

```
kafka-console-producer.sh --broker-list kafka1:9092,kafka2:9092,kafka3:9092 --topic jin-topic
```

```
kafka-console-consumer.sh --bootstrap-server kafka1:9092,kafka2:9092,kafka3:9092 --topic jin-topic --from-beginning
```
