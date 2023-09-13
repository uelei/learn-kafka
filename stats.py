from kafka import KafkaConsumer, TopicPartition

TOPIC = "vaifilhao"
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(
                         group_id='status',
                         bootstrap_servers=['192.168.1.228:19092'])


topics = consumer.topics()

print(f"the topics are {topics}")

partitions = consumer.partitions_for_topic(TOPIC)

print(f"partitions for topic {TOPIC}: {partitions}")


for part in partitions:
    p = TopicPartition(TOPIC,part)
    consumer.assign([p])
    offset = consumer.position(p)
    print(f"The offset of the partition {part} is {offset} of the topic {TOPIC}")

