"""
Global variables
"""

# Kafka config variables
KAFKA_SERVER: str = 'localhost:9092';

# PLOAM messages types
PLOAM_DEACTIVATE_MESSAGE: int = 5
PLOAM_ASSIGN_ONUID_MESSAGE: int = 3
PLOAM_RANGING_TIME_MESSAGE: int = 4
PLOAM_ASSIGN_ALLOCID_MESSAGE: int = 10
PLOAM_CONFIGURE_PORTID_MESSGAE: int = 14
PLOAM_BER_INTERVAL_MESSAGE: int = 18
PLOAM_EMPTY_MESSAGE: int = 11

# GPON frames producent configuration
PATH: str = r"/home/pancinator/Documents/DP/gpon_frames"

# Topics with processed data
PLOAM_MESSAGES_BY_TYPE_1: str = 'PloamType1'
PLOAM_MESSAGES_BY_TYPE_3: str = 'PloamType3'
PLOAM_MESSAGES_BY_TYPE_4: str = 'PloamType4'
PLOAM_MESSAGES_BY_TYPE_8: str = 'PloamType8'

CONNECTED_ONUS: str = 'ConnectedOnus'
UNIQUE_PLOAM_MESSAGES = 'UniquePloamMessages'

PLOAM_MESSAGES_BY_ONUID_0: str = 'PloamOnuid0'