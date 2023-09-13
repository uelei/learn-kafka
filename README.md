# Kafka

## To start a basic server kafka + zookeeper


```sh
docker compose -f docker-compose-single.yaml up -d
```

## To start 3 Kafka + zookeeper + schema registry

```sh
docker compose -f docker-compose-3-kafka.yaml up -d
```


## To check status of the kafka cluster/topic

```sh
wget https://www.apache.org/dyn/closer.cgi?path=/kafka/3.5.0/kafka_2.13-3.5.0.tgz
tar -xzf kafka_2.13-3.5.0.tgz
cd kafka_2.13-3.5.0

./kafka-topics.sh --describe --bootstrap-server localhost:19092 --topic vaifilhao

./kafka-topics.sh --topic vaifilhao --alter --partitions 4  --bootstrap-server localhost:19092

```
