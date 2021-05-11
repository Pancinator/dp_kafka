# dp-kafka

### Source files for diploma thesis of Matej Pancák

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
    - messages
      (Classes of produced messages)
        - unique_ploam_message_format.py
        - connected_onus_message_format.py
        - filter_ploam_messages_by_type_format.py
        - messages_format.py
        - messages_types.py
    - filter_unique_onus.py
    - filter_unique_ploam_messages.py

    - kafka_services
      (service and configuration files important for managing connections with apache kafka)
        - config.py (global configuration variables)
        - kafka_services.py

    - main.py (running class)
    - process_frames.py (process raw data from kafka)

    - read_gpon_frames.py (example of processing frames from .txt files)

### Inštalácia

1. Mať nainštalovaný docker a docker-compose
2. Naklonovať repozitár
3. Mať spustený Kafka cluster dostupný z https://github.com/Pancinator/dp_dockerize_kafka
4. V terminálovom okne spustenom v naklonovanom repozitáry spustiť príkaz docker-compose up
5. Ak sa v Kafke nachádzajú správy na spracovanie, proces filtrácie sa začne a v terminálovom okne sa obiavia konzolové výstupy


