"""
Example of kafka consumer subscribing topic ConnectedOnus -> will be used in web app backend
"""


from kafka import KafkaConsumer
from dp_kafka.src.kafka_services import config
from json import loads

consumer = KafkaConsumer('PloamOnuId1',
                         bootstrap_servers=[config.KAFKA_SERVER],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='my-group',
                         value_deserializer=lambda data: loads(data.decode('utf-8')),
                         api_version=(0, 10, 1))

for message in consumer:
    print(message.value)
