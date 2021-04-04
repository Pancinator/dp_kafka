"""
Class specifying shape of message publishing to topic kafka broker UniquePloamMessages
"""

import json
from datetime import datetime
from src.filters.messages_formats.messages_format import MessagesFormat


class UniquePloamMessagesFormat(MessagesFormat):
    ploam_message_id: int
    count: int
    ploam_message_name: str
    ploam_message_id_bin: str

    def __init__(self, ploam_message_id: int, frame_id: int, onu_id: int):
        super().__init__(onu_id, frame_id)
        self.ploam_message_id = ploam_message_id

    # doplnit metody pre ziskanie ploam_message_name a ploam_message_id_bin


