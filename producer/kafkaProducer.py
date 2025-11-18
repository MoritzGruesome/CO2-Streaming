from kafka import KafkaProducer
import requests
import time
import os
import pickle
import pprint

debug = "True" == os.environ['DEBUG'] # true when building directly from Dockerfile

print(f"debug is: {debug}")
print("producer script started")

connectionUp = False

headers = {
  'Accept': 'application/json'
}

if debug:   
    connectionUp = True
    r = requests.get('https://api.carbonintensity.org.uk/intensity', headers = headers)
    response = str(r.json()["data"][0]["intensity"]["actual"])
    print(f"actual CO2 level is: {response}")

while not connectionUp:
    try:

        producer = KafkaProducer(bootstrap_servers='kafka:9093')

        if producer.bootstrap_connected():

            r = requests.get('https://api.carbonintensity.org.uk/intensity', headers = headers)
            
            response = pickle.dumps(r.json()) # byte serialized

            print("trying to send now")
            producer.send('CO2level', response)
            
            producer.flush()
        
        connectionUp = True

    except Exception as e:
        print(e)

    time.sleep(1)




