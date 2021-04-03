"""
Class definition for Apache Kafka filter.
After initialization, the new producent instance is created.

Input:
    GPON frames
Output:
    Array of unique connected ONU ID's pushed to kafka broker, specifically to
    ConnectedOnus topic.
"""


import json
from kafka_services.kafka_services import initialize_producer


class FilterUniqueOnus:
    uniqueConnectedOnusIds = {'ConnectedOnus': [], 'FramesIdsOfUniqueOnus': []}
    producer = None

    def __init__(self):
        self.producer = initialize_producer()

    # Method for filtering
    def filter_connected_onus(self, message):
        frame_id_num = list(message.value.keys())[0]
        message_onu_id = message.value[frame_id_num]['PLOAMdownstream']['ONUid']

        # update list with newly connected onu's and push them to topic ConnectedOnus
        if message_onu_id not in self.uniqueConnectedOnusIds['ConnectedOnus']:
            self.uniqueConnectedOnusIds['ConnectedOnus'].append(message_onu_id)
            self.uniqueConnectedOnusIds['FramesIdsOfUniqueOnus'].append(frame_id_num)
            data = json.dumps(self.uniqueConnectedOnusIds)
            # Update ConnectedOnus topic
            self.producer.send('ConnectedOnus', value=data)
            print(data)
