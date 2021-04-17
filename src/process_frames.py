"""
This is the base consumer which consumes raw data from GPONFrames topic.
Messages in this consumer are then filtered and manipulated by filter instances
"""

from dp_kafka.src.filters.filter_connected_onus import FilterConnectedOnus
from dp_kafka.src.filters.filter_unique_ploam_messages import FilterUniquePloamMessages
from dp_kafka.src.filters.filter_ploam_messgaes_by_type import FilterPloamMessagesByType
from dp_kafka.src.filters.filter_ploam_messages_by_onuid import FilterPloamMessagesByOnuId
from dp_kafka.src.kafka_services.kafka_services import initialize_consumer
from datetime import datetime
import glob
import json
import ast


class ProcessFrames:
    consumer: initialize_consumer
    onus_filter: FilterConnectedOnus
    unique_ploam_messages_filter: FilterUniquePloamMessages
    connected_onus_filter: FilterConnectedOnus
    filter_ploam_messages_by_type: FilterPloamMessagesByType
    filter_ploam_messages_by_onu_id: FilterPloamMessagesByOnuId

    def __init__(self):
        self.consumer = initialize_consumer()
        self.unique_ploam_messages_filter = FilterUniquePloamMessages()
        self.connected_onus_filter = FilterConnectedOnus()
        self.ploam_messages_type_filter = FilterPloamMessagesByType()
        self.filter_ploam_messages_by_onu_id = FilterPloamMessagesByOnuId()

    def process(self):
        for message in self.consumer:
            # Filter messages in consumer
            self.connected_onus_filter.filter_connected_onus(message.value)
            self.ploam_messages_type_filter.filter_ploam_messages_by_type(message.value)
            self.filter_ploam_messages_by_onu_id.filter_ploam_messages_by_onu_id(message.value)
            self.unique_ploam_messages_filter.filter_unique_ploam_messages(message.value)







