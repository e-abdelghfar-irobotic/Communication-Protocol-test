import random
import time

from paho.mqtt import client as mqtt_client

from random import choice
from string import ascii_uppercase

broker = 'localhost'
port = 1883
topic = "Iroboticass123"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'

def connect_mqtt():
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

def publish(client):
    msg_count = 10000
    while True:
        time.sleep(0.1)# time to wait before publishing
        strmsg=''.join(choice(ascii_uppercase) for i in range(msg_count))
        msg = f"{strmsg}/{time.time()}" # publish message that contains the time being published
        result = client.publish(topic, payload=msg,qos=0,retain=False) 
        status = result[0]
        if status == 0: # if the message was successfully published
            pass
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 100000: # send 1000 messaged then break
            break

def run():
    client = connect_mqtt()
    time.sleep(3)
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()