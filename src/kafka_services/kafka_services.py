from kafka import KafkaProducer
from kafka_services import config
from kafka import KafkaConsumer
from json import loads
import json


def initialize_producer():
    producer = KafkaProducer(bootstrap_servers=[config.KAFKA_SERVER],
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                             api_version=(0, 10, 1))
    return producer


def initialize_consumer():
    consumer = KafkaConsumer('GPONFrames',
                             bootstrap_servers=[config.KAFKA_SERVER],
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             group_id='my-group',
                             value_deserializer=lambda data: loads(data.decode('utf-8')),
                             api_version=(0, 10, 1))
    return consumer
