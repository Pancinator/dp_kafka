from kafka_services.kafka_services import initialize_producer
from messages.filter_ploam_messages_by_onu_id_format import FilterMessagesByOnuIdFormat
from kafka import KafkaProducer
import json


class FilterPloamMessagesByOnuId:
    """
        Class which represents GPON filter instance. To process the message use method filter_ploam_messages_by_type
        with GPON frame in JSON format as argument. After initialization, the new producent instance is created.

        This filter pushes messages to separate topics by the connected ONU
        For more details pleas see docuemntation
    """

    buffer: dict

    def __init__(self):
        self.buffer = {}

    def filter_ploam_messages_by_onu_id(self, message, producer: KafkaProducer):
        """
            Method for frame processing
            :param producer: producer instance
            :param message: GPON frame in JSON format
            :return: Push message with additional information to separate topics by ONU ID
        """

        ploam_message_onu_id = message['PLOAMdownstream']['ONUid']
        ploam_message_id = message['PLOAMdownstream']['MessageID']
        ploam_message_data = message['PLOAMdownstream']['Data']

        if ploam_message_onu_id not in self.buffer.keys():
            self.buffer[ploam_message_onu_id] = []

        if ploam_message_id != 11:
            message = FilterMessagesByOnuIdFormat(ploam_message_id, ploam_message_onu_id, ploam_message_data)
            self.buffer[ploam_message_onu_id].append(message.__dict__)
            producer.send(f'PloamOnuId{ploam_message_onu_id}', value=json.dumps(self.buffer[ploam_message_onu_id]))





