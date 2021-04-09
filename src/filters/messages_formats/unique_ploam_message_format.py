"""
Class specifying shape of message publishing to topic kafka broker UniquePloamMessages
"""

import json
from datetime import datetime
from dp_kafka.src.filters.messages_formats.messages_format import MessagesFormat


class UniquePloamMessagesFormat(MessagesFormat):
    ploam_message_id: int
    count: int
    ploam_message_name: str
    ploam_message_id_bin: str
    counter: int

    def __init__(self, ploam_message_id: int, onu_id: int, counter: int):
        super().__init__(onu_id)
        self.ploam_message_id = ploam_message_id
        self.ploam_message_name = self.get_ploam_message_name()
        self.ploam_message_id_bin = self.get_ploam_message_name()
        self.counter = counter

    def get_ploam_message_name(self):
        return self.get_ploam_message_type(self.ploam_message_id)


    # doplnit metody pre ziskanie ploam_message_name a ploam_message_id_bin


