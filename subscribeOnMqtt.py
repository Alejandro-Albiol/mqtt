import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
host = "IP"
topic = "demo"
PORT = 1883
KEEPALIVE = 60

def on_connect(client, userdata, flags, rc):
        
        print(f"Connected to:\nHost: {host}\nTopic: {topic}")
        client.subscribe(topic)

def on_message(client, userdata, msg):
    
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

client.on_connect = on_connect
client.on_message = on_message

client.connect(host, PORT, KEEPALIVE)

client.loop_forever()