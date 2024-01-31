import random
from paho.mqtt import client as mqtt_client
import time
import sys
broker = 'localhost'
port = 1883
topic = "Iroboticass123"
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

counter=0

def get_size_of_string(string:str):
    encoded_bytes = string.encode("utf-8")
    size_in_bytes = len(encoded_bytes)
    return size_in_bytes

def subscribe(client: mqtt_client):
    global counter
    def on_message(client, userdata, msg):
        global counter
        counter += 1
        recevied:str=msg.payload.decode()
        re=recevied.split('/')
        print(f"message order is {counter}")
        print(f"    size is {get_size_of_string(recevied)}")
        print(f"    response time is {round(-float(re[1])+time.time(),8)} seconds")

    client.subscribe(topic)
    client.on_message = on_message # define a callback function

def run():
    client = connect_mqtt()
    subscribe(client) 
    client.loop_forever() 
    


if __name__ == '__main__':
    run()
