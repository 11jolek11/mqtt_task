import paho.mqtt.client as mqtt
import datetime
import psutil
import time

# TODO: Czy ja to wgl dobrze robię??!!
def battery_hook(client:mqtt.Client, topic:str) -> None:
    holder = psutil.sensors_battery().percent
    while True:
        time.sleep(1.5)
        temp = psutil.sensors_battery().percent
        if holder != temp:
            chain = str(temp) + " [" + str(datetime.datetime.now()) + "]"
            client.publish(topic, chain)
        holder = temp

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_publish(client, userdata, mid):
    print(">> SENT")

client = mqtt.Client()
client.on_publish=on_publish
client.on_connect=on_connect

client.connect("test.mosquitto.org", 1883)

# psutil.sensors_battery()
# client.publish("topic/test", "Hello World")
battery_hook(client, "topic/test")

client.disconnect()
