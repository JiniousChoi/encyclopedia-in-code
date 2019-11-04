# Exercise for Ch02

## How to start up the replicated zookeeper cluster and multiple kafka brokers

```
docker-compose up -d
```

## Check if zookeepers form a cluster and its status

```
echo stat | nc -v localhost 2181
echo stat | nc -v localhost 2182
echo stat | nc -v localhost 2183
```

## How to start zk client and run 'ls /jin-topics/brokers/ids'

```
docker exec -i zoo1 zkCli.sh 
docker exec -i zoo2 zkCli.sh 
docker exec -i zoo3 zkCli.sh 
```

## How to create a topic named 'jin-topic'

```
docker exec -i kafka1 /opt/kafka/bin/kafka-topics.sh --zookeeper zoo1:2181,zoo2:2181,zoo3:2181/jin-kafka --replication-factor=1 --partitions 1 --topic jin-topic --create
docker exec -i kafka2 /opt/kafka/bin/kafka-topics.sh --zookeeper zoo1:2181,zoo2:2181,zoo3:2181/jin-kafka --replication-factor=1 --partitions 1 --topic jin-topic --create
docker exec -i kafka3 /opt/kafka/bin/kafka-topics.sh --zookeeper zoo1:2181,zoo2:2181,zoo3:2181/jin-kafka --replication-factor=1 --partitions 1 --topic jin-topic --create
```

## How to punch in some messages in a topic

```
docker exec -i kafka1 /opt/kafka/bin/kafka-console-producer.sh --broker-list kafka1:9092,kafka2:9092,kafka3:9092 --topic jin-topic
docker exec -i kafka2 /opt/kafka/bin/kafka-console-producer.sh --broker-list kafka1:9092,kafka2:9092,kafka3:9092 --topic jin-topic
docker exec -i kafka3 /opt/kafka/bin/kafka-console-producer.sh --broker-list kafka1:9092,kafka2:9092,kafka3:9092 --topic jin-topic
```

## Consuming kafka topic

```
docker exec -i kafka1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server kafka1:9092,kafka2:9092,kafka3:9092 --topic jin-topic --from-beginning
docker exec -i kafka2 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server kafka1:9092,kafka2:9092,kafka3:9092 --topic jin-topic --from-beginning
docker exec -i kafka3 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server kafka1:9092,kafka2:9092,kafka3:9092 --topic jin-topic --from-beginning
```
