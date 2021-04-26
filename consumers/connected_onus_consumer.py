"""
Example of kafka consumer subscribing topic ConnectedOnus -> will be used in web app backend
"""

from json import loads

from kafka import KafkaConsumer

from dp_kafka.src.kafka_services import config

consumer = KafkaConsumer('GPONFrames',
                         bootstrap_servers=[config.KAFKA_SERVER],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='my-group',
                         value_deserializer=lambda data: loads(data.decode('utf-8')),
                         api_version=(0, 10, 1))

for message in consumer:
    print(message.value)
