"""
Example of kafka consumer subscribing topic PloamType4
"""

from kafka_services import config
import basic_consumer

if __name__ == "__main__":
    frame_prodcuer = basic_consumer.BasicConsumer(config.PLOAM_MESSAGES_BY_TYPE_4)
    frame_prodcuer.print_messages()
