from time import sleep
from json import dumps
from kafka import KafkaProducer
import glob
import json
import ast

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
    with open(file, 'r') as f:
        response = json.dumps(f.read())
        response = ast.literal_eval(json.loads(response))

        # Iterate through JSON objects (frames)
        for i in range(1, len(response) - 1):
            data = {i: response[i]}
            producer.send('GPONFrames', value=data)




