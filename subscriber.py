import paho.mqtt.client as mqtt
import psutil
import requests
import json

# This is the Subscriber
topic = "testiot43"

def on_connect(client, userdata, flags, rc):
  print("Connected with result code: " + str(rc))
  client.subscribe(topic)

def on_message(client, userdata, msg):
    headers = {'Content-Type': 'application/json'}
    # TODO: Add: sending post req with json data
    content = msg.payload.decode()
    print(content)
    content = content.split('$')
    payload = json.dumps({
      "value": content[0],
      "timestamp": content[1]
    })

    url = "http://127.0.0.1:5001/add/" + topic

    response = requests.request("POST", url, headers=headers, data=payload)

    
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org",1883)

client.loop_forever()
