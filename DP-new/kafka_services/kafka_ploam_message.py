"""
Class specifying shape of message publishing to kafka broker
"""

import json
from datetime import datetime


def date_converter(o):
    if isinstance(o, datetime):
        return o.__str__()


class KafkaUniquePloamMessage:
    ploam_message_id = ''
    frame_id = ''
    onu_id = ''
    date = ''

    def __init__(self, ploam_message_id, frame_id, onu_id, date):
        self.ploam_message_id = ploam_message_id
        self.frame_id = frame_id
        self.onu_id = onu_id
        self.date = date

    def format_message(self):
        return json.dumps(self.__dict__, default=date_converter)

