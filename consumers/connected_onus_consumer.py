"""
Example of kafka consumer subscribing topic ConnectedOnus
"""

from kafka import KafkaConsumer
from kafka_services import config
from json import loads
import basic_consumer

if __name__ == "__main__":
    frame_prodcuer = basic_consumer.BasicConsumer(config.CONNECTED_ONUS)
    frame_prodcuer.print_messages()