from kafka import KafkaConsumer
import time 

time.sleep(20)
print("script started")
consumer = KafkaConsumer('exampleTopic',
                         bootstrap_servers='kafka:9093',
                         auto_offset_reset='earliest')
print("consumer started")
for msg in consumer:
    print(msg)