"""
This is the base consumer which consumes raw data from GPONFrames topic.
Messages in this consumer are then filtered and manipulated by filter instances
"""
from kafka import TopicPartition

from filters.filter_connected_onus import FilterConnectedOnus
from filters.filter_unique_ploam_messages import FilterUniquePloamMessages
from filters.filter_ploam_messgaes_by_type import FilterPloamMessagesByType
from filters.filter_ploam_messages_by_onuid import FilterPloamMessagesByOnuId
from kafka_services.kafka_services import initialize_consumer
from kafka_services.kafka_services import initialize_producer
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
        print('CREATING CONSUMER 1')
        self.consumer = initialize_consumer()
        self.consumer.assign([TopicPartition('GPONFrames', 0)])
        for message in self.consumer:
            # Filter messages in consumer
            self.connected_onus_filter.filter_connected_onus(message.value, self.producer)
            self.ploam_messages_type_filter.filter_ploam_messages_by_type(message.value, self.producer)
            self.filter_ploam_messages_by_onu_id.filter_ploam_messages_by_onu_id(message.value, self.producer)
            self.unique_ploam_messages_filter.filter_unique_ploam_messages(message.value, self.producer)

    def process_thread_2(self):
        print('CREATING CONSUMER 2')
        self.consumer2 = initialize_consumer()
        self.consumer2.assign([TopicPartition('GPONFrames', 1)])
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