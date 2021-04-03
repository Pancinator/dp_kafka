@ECHO OFF
ECHO Kafka create kafka topics
CALL E:\kafka\bin\windows\kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic GPONFrames
PAUSE