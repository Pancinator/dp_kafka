"""
Class definition for Apache Kafka filter.
After initialization, the new producent instance is created.

Input:
    GPON frames
Output:
    Array of unique connected ONU ID's pushed to kafka broker, specifically to
    ConnectedOnus topic.
    """
from kafka_services.kafka_ploam_message import KafkaUniquePloamMessage
from kafka_services.kafka_services import initialize_producer
from datetime import datetime


class FilterUniquePloamMessages:
    used_ploam_messages_dict = {}
    producer = None
    buffer = []

    def __init__(self):
        self.producer = initialize_producer()

    # Method for filtering
    def filter_unique_ploam_messages(self, message):
        frame_id_num = list(message.value.keys())[0]
        ploam_message_onu_id = message.value[frame_id_num]['PLOAMdownstream']['ONUid']
        ploam_message_id = message.value[frame_id_num]['PLOAMdownstream']['MessageID']

        if ploam_message_id not in self.used_ploam_messages_dict.keys():
            # Update used dict
            self.used_ploam_messages_dict[ploam_message_id] = [ploam_message_onu_id]

            # Create new json object
            message = KafkaUniquePloamMessage(ploam_message_id, frame_id_num, ploam_message_onu_id, datetime.now())
            data = message.format_message()
            self.buffer.append(data)

            # Update UniquePloamMessages topic
            self.producer.send('UniquePloamMessages', value=self.buffer)
            print(self.buffer)
        elif ploam_message_onu_id not in self.used_ploam_messages_dict[ploam_message_id]:
            self.used_ploam_messages_dict[ploam_message_id].append(ploam_message_onu_id)

            # Create new json object
            message = KafkaUniquePloamMessage(ploam_message_id, frame_id_num, ploam_message_onu_id, datetime.now())
            data = message.format_message()
            self.buffer.append(data)

            # Update UniquePloamMessages topic
            self.producer.send('UniquePloamMessages', value=self.buffer)
            print(self.buffer)
        else:
            pass
