from kafka import KafkaProducer
import time

print("producer script started")
time.sleep(10)
producer = KafkaProducer(bootstrap_servers='kafka:9093')
for i in range(10):
    producer.send('exampleTopic', b'some_message')

producer.flush()

