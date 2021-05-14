"""
Example of kafka consumer subscribing topic PloamType1
"""

from kafka import KafkaConsumer
from kafka_services import config
from json import loads
import basic_consumer

if __name__ == "__main__":
    frame_prodcuer = basic_consumer.BasicConsumer(config.PLOAM_MESSAGES_BY_TYPE_1)
    frame_prodcuer.print_messages()
