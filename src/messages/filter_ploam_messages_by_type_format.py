"""
Class specifying shape of message publishing to topic kafka broker PloamTypeX
"""

from messages.messages_format import MessagesFormat
from messages.messages_types import get_message_type_by_id


class FilterMessagesByTypeFormat(MessagesFormat):
    ploam_message_id: int
    ploam_message_name: str
    ploam_message_id_bin: str
    data: str

    def __init__(self, ploam_message_id: int, onu_id: int, data: str):
        super().__init__(onu_id)
        self.ploam_message_id = ploam_message_id
        self.data = data
        self.ploam_message_name = self.get_ploam_message_name()
        self.ploam_message_id_bin = self.get_ploam_message_name()

    def get_ploam_message_name(self):
        return get_message_type_by_id(self.ploam_message_id)
