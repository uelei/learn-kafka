from kafka import KafkaProducer
from kafka.errors import KafkaError
from datetime import datetime
from time import sleep

producer = KafkaProducer(bootstrap_servers=['192.168.1.228:19092', '192.168.1.228:39092', '192.168.1.228:29092' ])

TOPIC = "vaifilhao"

# Asynchronous by default
# Successful result returns assigned partition and offset
# print (record_metadata.topic)
# print (record_metadata.partition)
# print (record_metadata.offset)
#
# # produce keyed messages to enable hashed partitioning
# producer.send('my-topic', key=b'foo', value=b'bar')
#
# # encode objects via msgpack
# producer = KafkaProducer(value_serializer=msgpack.dumps)
# producer.send('msgpack-topic', {'key': 'value'})
#
# # produce json messages
# producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
# producer.send('json-topic', {'key': 'value'})
#
# produce asynchronously
while True:
    now = datetime.now().isoformat()
    msg = f"msg now is {now} "
    print(f"enviando {msg}")
    producer.send(TOPIC, msg.encode())
    sleep(5)
#
# def on_send_success(record_metadata):
#     print(record_metadata.topic)
#     print(record_metadata.partition)
#     print(record_metadata.offset)
#
# def on_send_error(excp):
#     print('I am an errback', excp)
#     # handle exception
#
# # produce asynchronously with callbacks
# producer.send('mytopic', b'raw_bytes').add_callback(on_send_success).add_errback(on_send_error)
#
# # block until all async messages are sent
# producer.flush()
#
# # configure multiple retries
# # producer = KafkaProducer(retries=5)
