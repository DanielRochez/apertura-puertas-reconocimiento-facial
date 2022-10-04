# Importar Bilbioteca
from numpy import identity
from deepface import DeepFace
import pandas as pd
from paho.mqtt import client as mqtt_client
import random
import time

from paho.mqtt import client as mqtt_client
broker = '127.0.0.1'
port = 1883
topic = "codigoIoT/mqtt/python"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish2(client,mensaje):
   # while True:
    time.sleep(1)
    msg = mensaje
    result = client.publish(topic, msg)
    time.sleep(1)
    print (result)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

# Buscar Rostro
print ("Buscando rostro")

# df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
df = DeepFace.find (img_path = "/home/daniel/Documentos/GitHub/apertura-puertas-reconocimiento-facial/deepface/faces/image2.jpeg", db_path = "/home/daniel/Documentos/GitHub/apertura-puertas-reconocimiento-facial/deepface/my_bd", enforce_detection = "false")
print ("Resultado ")
print (df)
print ("Seleccion")
print (df.identity[0])

client = connect_mqtt()
client.loop_start()
publish2(client,df.identity[0])