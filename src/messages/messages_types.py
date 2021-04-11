
"""
    Static class (not really a class) with ploam messages type dict and related methods.
"""


messages_types_dict = {
    "PLOAM_DEACTIVATE_MESSAGE": 5,
    "PLOAM_ASSIGN_ONUID_MESSAGE": 3,
    "PLOAM_RANGING_TIME_MESSAGE": 4,
    "PLOAM_ASSIGN_ALLOCID_MESSAGE": 10,
    "PLOAM_CONFIGURE_PORTID_MESSGAE": 14,
    "PLOAM_BER_INTERVAL_MESSAGE": 18,
    "PLOAM_EMPTY_MESSAGE": 11
}


def get_message_type_by_id(ploam_message_id: int):
    for message_type in messages_types_dict.keys():
        if messages_types_dict[message_type] == ploam_message_id:
            return message_type

    return "UNKNOWN TYPE"


def get_message_type_by_name(ploam_message_name: int):
    for message_type in messages_types_dict.keys():
        if message_type == ploam_message_name:
            return message_type

    return "UNKNOWN TYPE"
