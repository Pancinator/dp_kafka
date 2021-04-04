"""
Parent Class for other message formats classes
"""

import json
from datetime import datetime


class MessagesFormat:
    onu_id: int
    frame_id: int
    date: datetime

    def __init__(self, onu_id, frame_id):
        self.frame_id = frame_id
        self.onu_id = onu_id

    def date_converter(o):
        if isinstance(o, datetime):
            return o.__str__()

    def format_message(self):
        return json.dumps(self.__dict__, default=self.date_converter)

    def get_ploam_message_type(self, ploam_message_id: int = 11):
        switcher={
            5: 'PLOAM_DEACTIVATE_MESSAGE',
            3: 'PLOAM_ASSIGN_ONUID_MESSAGE',
            4: 'PLOAM_RANGING_TIME_MESSAGE',
            10: 'PLOAM_ASSIGN_ALLOCID_MESSAGE',
            14: 'PLOAM_CONFIGURE_PORTID_MESSGAE',
            18: 'PLOAM_BER_INTERVAL_MESSAGE',
            11: 'PLOAM_EMPTY_MESSAGE'
        }
        return switcher.get(ploam_message_id, 'PLOAM_EMPTY_MESSAGE')