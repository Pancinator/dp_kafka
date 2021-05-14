from messages.unique_ploam_message_format import UniquePloamMessagesFormat
from kafka_services.kafka_services import initialize_producer
from kafka import KafkaProducer


class FilterUniquePloamMessages:
    """
        Class which represents GPON filter instance. To process the message use method filter_unique_ploam_messages with
        GPON frame in JSON format as parameter. After initialization, the new producent instance is created.

        For more details please see documentation
    """

    used_ploam_messages_dict: dict
    producer: initialize_producer
    buffer: dict

    def __init__(self):
        self.used_ploam_messages_dict = {}
        self.buffer = {}

    # Method for filtering
    def filter_unique_ploam_messages(self, message, producer: KafkaProducer):
        """
        Method for frame processing
        :param producer: producer instance
        :param message: GPON frame in JSON format
        :return: Updating UniquePloamMessages topic in Kafka
        """
        ploam_message_onu_id = message['PLOAMdownstream']['ONUid']
        ploam_message_id = message['PLOAMdownstream']['MessageID']

        if ploam_message_onu_id not in self.used_ploam_messages_dict.keys():
            # Update used dict with new active ONU
            self.used_ploam_messages_dict[ploam_message_onu_id] = {}

            # Check if message type is present for detected ONU, if it is, increase counter, if not create new record
            self.update_used_messages_count(ploam_message_onu_id, ploam_message_id)

            # Create new record for buffer => data to be send to kafka broker
            self.buffer[ploam_message_onu_id]: dict = {}

            # Update buffer
            self.update_buffer(ploam_message_onu_id, ploam_message_id)

            # Update message count
            self.update_used_messages_count(ploam_message_onu_id, ploam_message_id)

            # Update UniquePloamMessages topic
            producer.send('UniquePloamMessages', value=self.buffer)
            print('PLOAM MESSAGES: ', self.buffer)
        else:
            # Check if message type is present for detected ONU, if it is, increase counter, if not create new record
            self.update_used_messages_count(ploam_message_onu_id, ploam_message_id)

            # Update buffer
            self.update_buffer(ploam_message_onu_id, ploam_message_id)

            # Update UniquePloamMessages topic
            producer.send('UniquePloamMessages', value=self.buffer)

    def get_ploam_message_type_count(self, ploam_message_onu_id, ploam_message_id):
        return self.used_ploam_messages_dict[ploam_message_onu_id][ploam_message_id]

    def update_used_messages_count(self, ploam_message_onu_id, ploam_message_id):
        if self.used_ploam_messages_dict[ploam_message_onu_id].get(ploam_message_id, False):
            self.used_ploam_messages_dict[ploam_message_onu_id][ploam_message_id] += 1
        else:
            self.used_ploam_messages_dict[ploam_message_onu_id][ploam_message_id] = 1

    def update_buffer(self, ploam_message_onu_id, ploam_message_id):
        if self.buffer[ploam_message_onu_id].get(ploam_message_id, False) is False:
            counter = self.get_ploam_message_type_count(ploam_message_onu_id, ploam_message_id)

            # Create new json data object with information about current ploam message
            message = UniquePloamMessagesFormat(
                ploam_message_id,
                ploam_message_onu_id,
                counter
            )
            self.buffer[ploam_message_onu_id][ploam_message_id]: dict = {}
            self.buffer[ploam_message_onu_id][ploam_message_id] = message.__dict__

        else:
            # Get message count
            count = self.get_ploam_message_type_count(ploam_message_onu_id, ploam_message_id)
            self.buffer[ploam_message_onu_id][ploam_message_id]['counter'] = count

