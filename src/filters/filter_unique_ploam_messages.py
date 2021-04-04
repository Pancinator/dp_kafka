"""
Class definition for Apache Kafka filter.
After initialization, the new producent instance is created.

Input:
    GPON frames
Output:
    Array of unique connected ONU ID's pushed to kafka broker, specifically to
    ConnectedOnus topic.
    """

from src.filters.messages_formats.unique_ploam_message_format import UniquePloamMessagesFormat
from src.kafka_services.kafka_services import initialize_producer
from src.kafka_services.config import PLOAM_EMPTY_MESSAGE


class FilterUniquePloamMessages:
    used_ploam_messages_dict: dict
    used_ploam_onu_ids: list
    producer: initialize_producer
    buffer: any
    """
     vyuzit pomocne dictionary kde bude platit {<onu_id>:{<message_id>:count}
    """


    def __init__(self):
        self.producer = initialize_producer()

    # Method for filtering
    def filter_unique_ploam_messages(self, message):
        frame_id_num: int = list(message.value.keys())[0]
        ploam_message_onu_id: int = message.value[frame_id_num]['PLOAMdownstream']['ONUid']
        ploam_message_id: int = message.value[frame_id_num]['PLOAMdownstream']['MessageID']

        if ploam_message_onu_id not in self.used_ploam_messages_dict.keys():
            # Update used dict
            self.used_ploam_messages_dict[ploam_message_onu_id] = []

            # Create new json object
            message = UniquePloamMessagesFormat(ploam_message_id, frame_id_num, ploam_message_onu_id)

            data = message.format_message()
            self.buffer.append(data)

            # Update UniquePloamMessages topic
            self.producer.send('UniquePloamMessages', value=self.buffer)
            print('PLOAM MESSAGES: ', self.buffer)

        """
                elif ploam_message_onu_id not in self.used_ploam_messages_dict[ploam_message_id]:
            self.used_ploam_messages_dict[ploam_message_id].append(ploam_message_onu_id)

            # Create new json object
            message = UniquePloamMessagesFormat(ploam_message_id, frame_id_num, ploam_message_onu_id, datetime.now())
            data = message.format_message()
            self.buffer.append(data)

            # Update UniquePloamMessages topic
            self.producer.send('UniquePloamMessages', value=self.buffer)
            print(self.buffer)
        else:
            pass

        """
    # doplnit metody pre ziskanie poctu sprav daneho typu