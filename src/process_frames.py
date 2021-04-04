"""
This is the base consumer which consumes raw data from GPONFrames topic.
Messages in this consumer are then filtered and manipulated by filter instances
"""

from src.filters.filter_connected_onus import FilterConnectedOnus
from src.filters.filter_unique_ploam_messages import FilterUniquePloamMessages
from src.kafka_services.kafka_services import initialize_consumer


class ProcessFrames:
    # Class parameters
    consumer: initialize_consumer = None
    onus_filter: FilterConnectedOnus = FilterConnectedOnus()
    ploam_messages_filter: FilterUniquePloamMessages = FilterUniquePloamMessages()

    # Create Kafka consumer instance in constructor
    def __init__(self):
        self.consumer = initialize_consumer()
        # Process incoming messages

    def process(self):
        for message in self.consumer:
            # Filter messages in consumer
            self.onus_filter.filter_connected_onus(message)
            self.ploam_messages_filter.filter_unique_ploam_messages(message)





