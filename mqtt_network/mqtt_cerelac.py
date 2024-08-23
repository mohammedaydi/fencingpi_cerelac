import time
import paho.mqtt.client as mqtt

client = mqtt.Client("rpi_client2")
flag_connected = 0

def on_publish(client, userdata, mid):
    print("message published")

def initialize_mqtt():
    #sending code---
    global client
    client = mqtt.Client("rpi_client2") #this name should be unique
    client.on_publish = on_publish
    client.connect('127.0.0.1',1883)
    # start a new thread
    client.loop_start()
    
    #receiving code---
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.message_callback_add('esp32/purple', callback_esp32_purple)
    client.message_callback_add('esp32/black', callback_esp32_black)
    #client.connect('127.0.0.1',1883)
    # start a new thread
    client.loop_start()
    client_subscriptions(client)
    print("......client setup complete............")

#--------------------------------------

def on_connect(client, userdata, flags, rc):
   global flag_connected
   flag_connected = 1
   client_subscriptions(client)
   print("Connected to MQTT server")

def on_disconnect(client, userdata, rc):
   global flag_connected
   flag_connected = 0
   print("Disconnected from MQTT server")
   
# a callback functions 
def callback_esp32_black(client, userdata, msg):
    print('black ESP data: ', str(msg.payload.decode('utf-8')))

def callback_esp32_purple(client, userdata, msg):
    print('purple ESP data: ', str(msg.payload.decode('utf-8')))

def client_subscriptions(client):
    client.subscribe("esp32/black")
    client.subscribe("esp32/purple")



