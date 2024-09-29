import paho.mqtt.client as mqtt
import time
client = mqtt.Client()
host = "IP"
topic = "demo"
message = "Test 1"
PORT = 1883
KEEPALIVE = 60

def on_connect():
    print(f"Connected to:\nHost: {host}\nTopic: {topic}")
    client.connect(host, PORT, KEEPALIVE)

while True:

    client.publish(topic, message)
    print(f"'{message}' enviado a '{topic}'")
    time.sleep(5)
