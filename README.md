# dp-kafka

Source files for diploma thesis of Matej Pancák

Repository structure:
- consumers
  (consumers examples for web app backend)
  - connected_onus_consumer.py
  - unique_ploam_messages_consumer.py
  
- producents
  (producent example, using for producing messages from text files)
  - producent.py
  
- src 
  (source files for GPON frames filter)
  - filters
    (scripts for filtering needed informations from consumed messages)
    - messgae_formats 
      (Classes of produced messages)
      - unique_ploam_message_format.py
    - filter_unique_onus.py
    - filter_unique_ploam_messages.py
    
  - kafka_services
    (service and configuration files important for managing connections with apache kafka)
    - config.py (global configuration variables)
    - kafka_services.py
    
  - main.py (running class)
  - process_frames.py (process raw data from kafka)
    
  - read_gpon_frames.py (example of processing frames from .txt files)