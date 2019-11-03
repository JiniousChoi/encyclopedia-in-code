# Setup for kafka study on docker

```
docker network create kafka-study
```

```
docker run -d --name zookeeper -p 2181:2181 --network kafka-study dockerkafka/zookeeper
```

```
docker run -d --name kafka -p 9092:9092 --network kafka-study dockerkafka/kafka
```

```
docker exec kafka ping kafka
docker exec zookeeper ping zookeeper
docker exec kafka ping zookeeper
docker exec zookeeper ping kafka
```
