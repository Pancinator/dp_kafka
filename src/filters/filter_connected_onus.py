"""
Class definition for Apache Kafka filter.
After initialization, the new producent instance is created.

Input:
    GPON frames
Output:
    Array of unique connected ONU ID's pushed to kafka broker, specifically to
    ConnectedOnusActive and ConnectedOnusDeactivated topic.
"""

from kafka_services.kafka_services import initialize_producer
from messages.connected_onus_message_format import ConnectedOnusMessageFormat
from kafka_services.config import PLOAM_DEACTIVATE_MESSAGE
import json
from datetime import datetime


class FilterConnectedOnus:
    """
        Class definition for Apache Kafka filter.
        After initialization, the new producent instance is created.
        Contains method for processing and manipulating with GPON frames
    """
    unique_connected_onus_ids: list
    unique_deactivated_onus_ids: list
    buffer: dict
    producer: initialize_producer

    def __init__(self):
        # self.producer = initialize_producer()
        self.buffer = {'active': [], 'deactivated': []}
        self.unique_connected_onus_ids = []
        self.unique_deactivated_onus_ids = []

    def filter_connected_onus(self, message, producer):
        """
        Method for filtering connected ONU's, divide ONU's to active and deactivated lists
        :param message: GPON frame consumed from Kafka
        :return: produce information message to Kafka topic ConnectedOnus
        """

        message_onu_id: int = message['PLOAMdownstream']['ONUid']
        message_ploam_message_id: int = message['PLOAMdownstream']['MessageID']

        # update list with connected ONU's and push them to topic ConnectedOnus
        if message_onu_id not in self.unique_connected_onus_ids:
            # If ONU is on the deactivated ONU's list, remove it.
            if message_onu_id in self.unique_deactivated_onus_ids:
                self.unique_deactivated_onus_ids.remove(message_onu_id)

            # Update helper list
            self.unique_connected_onus_ids.append(message_onu_id)
            message: ConnectedOnusMessageFormat = ConnectedOnusMessageFormat(message_onu_id)
            data: dict = message.__dict__
            self.buffer['active'].append(data)

            # Update ConnectedOnus topic with buffered data
            producer.send('ConnectedOnus', value=self.buffer)

        elif message_onu_id in self.unique_connected_onus_ids and message_ploam_message_id == PLOAM_DEACTIVATE_MESSAGE:
            # remove ONU from buffer and push updated list to Kafka
            self.unique_connected_onus_ids.remove(message_onu_id)
            self.buffer['active'] = [message if message['onu_id'] != message_onu_id else "" for message in self.buffer['active']]

            message: ConnectedOnusMessageFormat = ConnectedOnusMessageFormat(message_onu_id)
            data: dict = message.format_message()
            self.buffer['deactivated'].append(data)

            # update helper list
            self.unique_deactivated_onus_ids.append(message_onu_id)
            producer.send('ConnectedOnus', value=self.buffer)




