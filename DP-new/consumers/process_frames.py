"""
This is the base consumer which consumes raw data from GPONFrames topic.
Messages in this consumer are then filtered and manipulated by filter instances
"""

from filters.filter_unique_onus import FilterUniqueOnus
from filters.filter_unique_ploam_messages import FilterUniquePloamMessages
from kafka_services import config
from kafka_services.kafka_services import initialize_consumer


class ProcessFrames():
    consumer = None
    onus_filter = FilterUniqueOnus()
    ploam_messages_filter = FilterUniquePloamMessages()

    # Create Kafka consumer instance in constructor
    def __init__(self):
        self.consumer = initialize_consumer()
        # Process incoming messages

    def process(self):
        for message in self.consumer:
            # Filter connected ONU
            self.onus_filter.filter_connected_onus(message)
            self.ploam_messages_filter.filter_unique_ploam_messages(message)





