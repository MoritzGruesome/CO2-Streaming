from kafka import KafkaConsumer
import time 
import pickle

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
            print("trying to deserialize")
            message = pickle.loads(msg) # deserialize
            print("printing message")
            print(message)
        
    except Exception as e:
        print(e)
    time.sleep(1)

