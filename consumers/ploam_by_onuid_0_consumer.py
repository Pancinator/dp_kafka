"""
Example of kafka consumer subscribing topic UniquePloamMessages
"""

from kafka import KafkaConsumer
from kafka_services import config
from json import loads
import basic_consumer

if __name__ == "__main__":
    frame_prodcuer = basic_consumer.BasicConsumer(config.PLOAM_MESSAGES_BY_ONUID_0)
    frame_prodcuer.print_messages()
