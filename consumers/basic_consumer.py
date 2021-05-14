"""
Example of kafka consumer subscribing topic ConnectedOnus -> will be used in web app backend
"""

from kafka import KafkaConsumer
from kafka_services import config
from json import loads
from kafka_services import config


class BasicConsumer:
    consumer: KafkaConsumer

    def __init__(self, topic: str):
        self.consumer = KafkaConsumer(topic,
                             bootstrap_servers=[config.KAFKA_SERVER],
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             group_id='my-group2',
                             value_deserializer=lambda data: loads(data.decode('utf-8')),
                             api_version=(0, 10, 1))

    def print_messages(self):
        for message in self.consumer:
            print(message.value)


