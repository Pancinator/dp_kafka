"""
This is the base consumer which consumes raw data from GPONFrames topic.
Messages in this consumer are then filtered and manipulated by filter instances
"""

from dp_kafka.src.filters.filter_connected_onus import FilterConnectedOnus
from dp_kafka.src.filters.filter_unique_ploam_messages import FilterUniquePloamMessages
from dp_kafka.src.filters.filter_ploam_messgaes_by_type import FilterPloamMessagesByType
from dp_kafka.src.filters.filter_ploam_messages_by_onuid import FilterPloamMessagesByOnuId
from dp_kafka.src.kafka_services.kafka_services import initialize_consumer
from dp_kafka.src.kafka_services.kafka_services import initialize_producer
from datetime import datetime
import glob
import json
import ast
import threading


class ProcessFrames:
    consumer: initialize_consumer
    consumer2: initialize_consumer
    onus_filter: FilterConnectedOnus
    unique_ploam_messages_filter: FilterUniquePloamMessages
    connected_onus_filter: FilterConnectedOnus
    filter_ploam_messages_by_type: FilterPloamMessagesByType
    filter_ploam_messages_by_onu_id: FilterPloamMessagesByOnuId
    producer: initialize_producer

    def __init__(self):
        self.unique_ploam_messages_filter = FilterUniquePloamMessages()
        self.connected_onus_filter = FilterConnectedOnus()
        self.ploam_messages_type_filter = FilterPloamMessagesByType()
        self.filter_ploam_messages_by_onu_id = FilterPloamMessagesByOnuId()
        self.producer = initialize_producer()

    def process_thread_1(self):
        print('creating consumer 1')
        self.consumer = initialize_consumer()
        for message in self.consumer:
            # Filter messages in consumer
            self.connected_onus_filter.filter_connected_onus(message.value, self.producer)
            self.ploam_messages_type_filter.filter_ploam_messages_by_type(message.value, self.producer)
            self.filter_ploam_messages_by_onu_id.filter_ploam_messages_by_onu_id(message.value, self.producer)
            self.unique_ploam_messages_filter.filter_unique_ploam_messages(message.value, self.producer)

    def process_thread_2(self):
        print('creating consumer 2')
        self.consumer2 = initialize_consumer()
        for message in self.consumer2:
            # Filter messages in consumer
            self.connected_onus_filter.filter_connected_onus(message.value, self.producer)
            self.ploam_messages_type_filter.filter_ploam_messages_by_type(message.value, self.producer)
            self.filter_ploam_messages_by_onu_id.filter_ploam_messages_by_onu_id(message.value, self.producer)
            self.unique_ploam_messages_filter.filter_unique_ploam_messages(message.value, self.producer)

    def start_threads(self):
        thread1 = threading.Thread(target= self.process_thread_1)
        thread2 = threading.Thread(target= self.process_thread_2)
        thread1.start()
        thread2.start()