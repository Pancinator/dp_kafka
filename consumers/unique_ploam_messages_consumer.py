from json import loads

from kafka import KafkaConsumer


#  Kafka consumer subscribing topic UniquePloamMessages -> will be used in web app backend of my colleague Pavel
consumer = KafkaConsumer('UniquePloamMessages',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='my-group',
                         value_deserializer=lambda data: loads(data.decode('utf-8')),
                         api_version=(0, 10, 1))

for message in consumer:
    print(message)
