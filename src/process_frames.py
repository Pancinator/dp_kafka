"""
This is the base consumer which consumes raw data from GPONFrames topic.
Messages in this consumer are then filtered and manipulated by filter instances
"""

from dp_kafka.src.filters.filter_connected_onus import FilterConnectedOnus
from dp_kafka.src.filters.filter_unique_ploam_messages import FilterUniquePloamMessages
from dp_kafka.src.filters.filter_ploam_messgaes_by_type import FilterPloamMessagesByType
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
    # Create Kafka consumer instance in constructor
    def __init__(self):
        self.consumer = initialize_consumer()
        self.onus_filter = FilterConnectedOnus()
        self.unique_ploam_messages_filter = FilterUniquePloamMessages()
        self.connected_onus_filter = FilterConnectedOnus()
        self.ploam_messages_type_filter = FilterPloamMessagesByType()

    def process(self):
        path = r"/Users/matejpancak/PycharmProjects/new_project_test/Tensor1.txt"
        files = glob.glob(path)
        respond = {}
        for file in files:
            with open(file, 'r') as f:
                response = json.dumps(f.read())
                response = ast.literal_eval(json.loads(response))
                print(datetime.now().__str__())
                for i in range(1, len(response)):
                    idct = {}
                    idct[i] = response[i]
                    # Filters
                    self.unique_ploam_messages_filter.filter_unique_ploam_messages(idct[i])
                    self.connected_onus_filter.filter_connected_onus(idct[i])
                    self.ploam_messages_type_filter.filter_ploam_messages_by_type(idct[i])

                print(datetime.now().__str__())


    """             
    
              for message in self.consumer:
        # Filter messages in consumer
        # self.onus_filter.filter_connected_onus(message)
    self.ploam_messages_filter.filter_unique_ploam_messages(message)
    """






