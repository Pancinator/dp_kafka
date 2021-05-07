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


# Path to stored Dataset
path = r"/home/pancinator/Documents/DP/gpon_frames"
files = glob.glob(f'{path}/*.txt')
respond = {}


def create_partitions():
    admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])
    topic_partitions = {}
    topic_partitions['GPONFrames'] = NewPartitions(total_count=2)
    admin_client.create_partitions(topic_partitions)

# Create producer instance with following configuration
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         api_version=(0, 10, 1))

threds = []


def process(file):
    with open(file, 'r') as f:
        response = json.dumps(f.read())
        response = ast.literal_eval(json.loads(response))

        # Iterate through JSON objects (frames)
        partition = 0
        for i in range(1, len(response) - 1):
            data = response[i]
            producer.send('GPONFrames', value=data)
            print(str(data))


# Iterate through all files from folder
for file in files:
    process(file)




