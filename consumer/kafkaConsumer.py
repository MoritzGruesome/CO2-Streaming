from kafka import KafkaConsumer
import time 
import json

print("script started")

connectionUp = False

while not connectionUp:

    try:
        consumer = KafkaConsumer('CO2level',
                                bootstrap_servers='kafka:9093',
                                auto_offset_reset='earliest')
        print("consumer connected successfully")

        connectionUp = True
        print("trying to read consumer data")
        for msg in consumer:
            
            message = json.loads(msg.value) # content is ASCII encoded, python prints based on UTF-8
            print("casting message")
            print(str(message["data"][0]["intensity"]["actual"]))

    except Exception as e:
        print(e)
    time.sleep(1)

