"""
Start producing frames from text files to GPONFrames topic
"""

import ast
import glob
import json

from kafka import KafkaProducer

# Path to stored Dataset
path = r"/home/pancinator/Documents/DP/gpon_frames"
files = glob.glob(f'{path}/*.txt')
respond = {}

# Create producer instance with following configuration
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         api_version=(0, 10, 1))

# Iterate through all files from folder
for file in files:
    print(file)
    with open(file, 'r') as f:
        response = json.dumps(f.read())
        response = ast.literal_eval(json.loads(response))

        # Iterate through JSON objects (frames)
        for i in range(1, len(response) - 1):
            data = response[i]
            producer.send('GPONFrames', value=data)
            print(data)
