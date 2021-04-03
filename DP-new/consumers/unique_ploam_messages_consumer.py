from kafka import KafkaConsumer
from kafka_services import config
from json import loads

#  Kafka consumer subscribing topic UniquePloamMessages -> will be used in web app backend of my colleague Pavel
consumer = KafkaConsumer('UniquePloamMessages',
                         bootstrap_servers=[config.KAFKA_SERVER],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='my-group',
                         value_deserializer=lambda data: loads(data.decode('utf-8')),
                         api_version=(0, 10, 1))

for message in consumer:
    print(message)
