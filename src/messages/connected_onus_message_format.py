"""
Class specifying shape of message publishing to topic kafka broker ConnectedOnusActive
"""

from dp_kafka.src.messages.messages_format import MessagesFormat
from datetime import datetime


class ConnectedOnusMessageFormat(MessagesFormat):
    date: str

    def __init__(self, onu_id):
        super().__init__(onu_id)
        self.date = datetime.now().__str__()



