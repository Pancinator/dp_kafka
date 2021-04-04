"""
Class definition for Apache Kafka filter.
After initialization, the new producent instance is created.

Input:
    GPON frames
Output:
    Array of unique connected ONU ID's pushed to kafka broker, specifically to
    ConnectedOnusActive and ConnectedOnusDeactivated topic.
"""


import json
from src.kafka_services.kafka_services import initialize_producer
from messages_formats.connected_onus_message_format import ConnectedOnusMessageFormat
from src.kafka_services.config import PLOAM_DEACTIVATE_MESSAGE
from datetime import datetime


class FilterConnectedOnus:
    unique_connected_onus_ids: list
    unique_deactivated_onus_ids: list
    buffer: list
    producer: initialize_producer

    def __init__(self):
        self.producer = initialize_producer()

    # Method for filtering
    def filter_connected_onus(self, message):
        frame_id: int = list(message.value.keys())[0]
        message_onu_id: int = message.value[frame_id]['PLOAMdownstream']['ONUid']
        message_ploam_message_id: int = message.value[frame_id]['PLOAMdownstream']['MessageID']

        # update list with connected ONU's and push them to topic ConnectedOnusActive
        if message_onu_id not in self.unique_connected_onus_ids:
            # If ONU is on the deactivated ONU's list, remove it.
            if message_onu_id in self.unique_deactivated_onus_ids:
                self.unique_deactivated_onus_ids.remove(message_onu_id)

            self.unique_connected_onus_ids.append(message_onu_id)

            message: ConnectedOnusMessageFormat = ConnectedOnusMessageFormat(message_onu_id, frame_id, datetime.now())
            data: dict = message.format_message()
            self.buffer.append(data)

            # Update ConnectedOnusActive topic with buffered data
            self.producer.send('ConnectedOnusActive', value=self.buffer)
            print('LIST OF ACTIVE ONUs: ', self.buffer)

        elif message_onu_id in self.unique_connected_onus_ids and message_ploam_message_id == PLOAM_DEACTIVATE_MESSAGE:
            # remove ONU from buffer and push updated list to Kafka
            self.unique_connected_onus_ids.remove(message_onu_id)
            self.buffer = [message for message in self.buffer if message['onu_id'] != message_onu_id]
            self.unique_deactivated_onus_ids.append(message_onu_id)

            self.producer.send('ConnectedOnusActive', value=self.buffer)
            self.producer.send('ConnectedOnusDeactivated', value=json.dumps(self.unique_deactivated_onus_ids))
            print('ONU WITH ID WAS REMOVED: ', message_onu_id, 'BUFFER STATUS: ', self.buffer)
            print('LIST OF DEACTIVATED ONUs: ', json.dumps(self.unique_deactivated_onus_ids))


