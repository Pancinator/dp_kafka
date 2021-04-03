@ECHO OFF
ECHO This command runs Batch files with Zookeeper and Kafka servers instances
START cmd /k CALL E:\kafka\run-zookeeper-server.bat
TIMEOUT 25
START cmd /k CALL E:\kafka\run-kafka-server.bat 
PAUSE