"""
Parent Class for other message formats classes
"""

import json
from datetime import datetime


class MessagesFormat:
    onu_id: int
    date: datetime

    def __init__(self, onu_id):
        self.onu_id = onu_id

    def date_converter(o):
        if isinstance(o, datetime):
            return o.__str__()

    def format_message(self):
        return json.dumps(self.__dict__, default=self.date_converter)

