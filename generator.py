import paho.mqtt.client as mqtt
import datetime
import psutil
import time

topic = "testiot43"

def battery_hook(client:mqtt.Client, topic:str, diff=0.1) -> None:
    holder = psutil.sensors_battery().percent
    while True:
        time.sleep(1.5)
        tim = datetime.datetime.now()
        temp = psutil.sensors_battery().percent
        print(temp)
        if holder - temp >= diff:
            chain = str(temp) + "$[" + str(tim) + "]"
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
battery_hook(client, "testiot43", 0)

client.disconnect()
