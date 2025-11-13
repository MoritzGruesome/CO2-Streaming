from kafka import KafkaProducer
import time

print("producer script started")

connectionUp = False

while not connectionUp:
    try:

        producer = KafkaProducer(bootstrap_servers='kafka:9093')

        if producer.bootstrap_connected():
            for i in range(10):
                producer.send('exampleTopic', b'some_message')
            
            producer.flush()
        
        connectionUp = True
    except:
        print("connection to broker failed")
    time.sleep(1)




