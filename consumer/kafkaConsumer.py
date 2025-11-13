from kafka import KafkaConsumer
import time 

print("script started")

connectionUp = False

while not connectionUp:

    try:
        consumer = KafkaConsumer('exampleTopic',
                                bootstrap_servers='kafka:9093',
                                auto_offset_reset='earliest')
        print("consumer connected successfully")

        connectionUp = True

        for msg in consumer:
            print(msg)
        
    except:
        print("consumer failed to connect to broker")
    time.sleep(1)

