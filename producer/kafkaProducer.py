from kafka import KafkaProducer
import requests
import time
import os
import json
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
    response_type = type(r.content)
    encoding_type = r.apparent_encoding
    print(f"actual CO2 level is: {response}")
    print(f"type of content: {response_type}")
    print(f"the apparent encoding {encoding_type}")

while not connectionUp:
    try:

        producer = KafkaProducer(bootstrap_servers='kafka:9093')

        if producer.bootstrap_connected():

            r = requests.get('https://api.carbonintensity.org.uk/intensity', headers = headers)

            print("trying to send now")
            response = bytes(json.dumps(r.json()), 'utf-8')


            producer.send('CO2level', response)
            
            producer.flush()
        
        connectionUp = True

    except Exception as e:
        print(e)

    time.sleep(1)




