from kafka import KafkaConsumer, TopicPartition
TOPIC = "vaifilhao"
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    auto_commit_interval_ms=1000,
    group_id='my-group3',
    bootstrap_servers=['192.168.1.228:19092'])



tp = TopicPartition(TOPIC, 0)
consumer.assign([tp])
consumer.seek_to_beginning()
consumer.seek(tp, 41)
# print(consumer.partitions_for_topic(TOPIC))
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

