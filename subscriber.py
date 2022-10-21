import paho.mqtt.client as mqtt
import psutil

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
    print(msg.payload.decode())
#   if msg.payload.decode() == "Hello world!":
    # print("Yes!")
    # client.disconnect()
    
client = mqtt.Client()


client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org",1883)


client.loop_forever()