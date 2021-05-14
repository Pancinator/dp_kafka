"""
Start producing frames from text files to GPONFrames topic
"""

from time import sleep
from json import dumps
from kafka import KafkaProducer
import glob
import json
import ast
import threading
from kafka import KafkaAdminClient
from kafka.admin import NewPartitions
from dp_kafka.src.kafka_services import config


class ProduceFrames:
    # Path to stored Dataset
    path: str
    files: list
    response: dict = {}
    partition: int
    producer: KafkaProducer

    def __init__(self):
        self.path = config.PATH
        self.files = glob.glob(f'{self.path}/*.txt')
        self.create_producer()
        self.partition = 0

    def create_partitions(self):
        admin_client = KafkaAdminClient(bootstrap_servers=[config.KAFKA_SERVER])
        topic_partitions = {'GPONFrames': NewPartitions(total_count=2)}
        admin_client.create_partitions(topic_partitions)

    def create_producer(self):
        # Create producer instance with following configuration
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                 api_version=(0, 10, 1))

    def switch_partition(self):
        if self.partition == 0:
            self.partition = 1
        else:
            self.partition = 0

    def process(self):
        for file in self.files:
            with open(file, 'r') as f:
                response = json.dumps(f.read())
                response = ast.literal_eval(json.loads(response))

                # Iterate through JSON objects (frames)
                for i in range(1, len(response) - 1):
                    data = response[i]
                    self.producer.send('GPONFrames', value=data, partition=self.partition)
                    print(str(data))
                    self.switch_partition()


if __name__ == "__main__":
    frame_prodcuer = ProduceFrames()
    frame_prodcuer.process()


