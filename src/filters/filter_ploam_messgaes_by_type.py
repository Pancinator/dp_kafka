from messages.unique_ploam_message_format import UniquePloamMessagesFormat
from kafka_services.kafka_services import initialize_producer
from messages.messages_types import messages_types_dict, get_message_type_by_id
from messages.filter_ploam_messages_by_type_format import FilterMessagesByTypeFormat
import json

class FilterPloamMessagesByType:
    """
        Class which represents GPON filter instance. To process the message use method filter_ploam_messages_by_type
        with GPON frame in JSON format as argument. After initialization, the new producent instance is created.

        This filter pushes messages to separate topics by the PLoam message type
        For more details pleas see docuemntation
    """

    buffer: dict

    def __init__(self):
        self.buffer = {}
        self.initialize_buffer()

    def filter_ploam_messages_by_type(self, message, producer):
        """
        Method for frame processing
        :param producer: producer instance
        :param message: GPON frame in JSON format
        :return: Push message with additional information to separate topics by type
        """

        ploam_message_onu_id = message['PLOAMdownstream']['ONUid']
        ploam_message_id = message['PLOAMdownstream']['MessageID']
        ploam_message_data = message['PLOAMdownstream']['Data']

        if ploam_message_id not in self.buffer.keys():
            self.buffer[ploam_message_id] = []

        if ploam_message_id != 11:
            message = FilterMessagesByTypeFormat(ploam_message_id, ploam_message_onu_id, ploam_message_data)
            self.buffer[ploam_message_id].append(message.__dict__)
            producer.send(f'PloamType{ploam_message_id}', value=self.buffer[ploam_message_id])

    def initialize_buffer(self):
        for key in messages_types_dict.keys():
            self.buffer[messages_types_dict[key]] = []




