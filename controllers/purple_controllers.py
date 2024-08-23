import time
from data.cerelac_data import purple
import RPi.GPIO as gpio

enPin = 11
stepPin = 10
directionPin = 9
is_initial = True
purple_front_switch = 20
purple_rear_switch = 21

hit_timer_delay = 4
shield_timer_delay = 3

def setup_pins():
    gpio.setmode(gpio.BCM)
    gpio.setup(enPin,gpio.OUT)
    gpio.setup(directionPin,gpio.OUT)
    gpio.setup(stepPin,gpio.OUT)
    gpio.setup(purple_front_switch,gpio.IN)
    gpio.setup(purple_rear_switch,gpio.IN)
    gpio.output(enPin,gpio.LOW)
    is_initial = False

def move_forward():

    if is_initial:
        setup_pins()

    gpio.output(directionPin,gpio.HIGH)
    time.sleep(0.01)
    for x in range(0,1600):
        switch1 = gpio.input(purple_front_switch)
        switch2 = gpio.input(purple_rear_switch)

        if switch2 == 0:
            break

        gpio.output(stepPin,gpio.HIGH)
        time.sleep(0.000600)
        gpio.output(stepPin,gpio.LOW)
        time.sleep(0.000600)
    gpio.cleanup()
    return {"state": "moved_forward"}

def move_backwards():
    if is_initial:
        setup_pins()
    gpio.output(directionPin,gpio.LOW)
    time.sleep(0.01)
    for x in range(0,1600):
        switch1 = gpio.input(purple_front_switch)
        switch2 = gpio.input(purple_rear_switch)

        if switch1 == 0:
            break

        gpio.output(stepPin,gpio.HIGH)
        time.sleep(0.000600)
        gpio.output(stepPin,gpio.LOW)
        time.sleep(0.000600)
    gpio.cleanup()
    return {"state": "moved_backward"}

def rotate_right():
    curr = time.time()
    if(curr - purple["hit_timer"] > hit_timer_delay):
        from mqtt_network.mqtt_cerelac import client
        try:
            msg = "side"
            pubMsg = client.publish(
                topic='rpi/purple',
                payload=msg.encode('utf-8'),
                qos=0,
            )
            pubMsg.wait_for_publish()
            print(pubMsg.is_published())
            purple["hit_timer"] = curr
        except Exception as e:
            print(e)
        return {"state": "side"}
    else:
        return{"state": "cooldown"}
        


def rotate_left():
    curr = time.time()
    if(curr - purple["hit_timer"]  > hit_timer_delay):
        from mqtt_network.mqtt_cerelac import client
        try:
            msg = "defend"
            pubMsg = client.publish(
                topic='rpi/purple',
                payload=msg,
                qos=0,
            )
            pubMsg.wait_for_publish()
            print(pubMsg.is_published())
            purple["hit_timer"] = curr
        except Exception as e:
            print(e)
        return{"state": "defend"}
    else:
        return {"state": "cooldown"}


def high():
    curr = time.time()
    if(curr - purple["hit_timer"] > hit_timer_delay):
        from mqtt_network.mqtt_cerelac import client
        try:
            msg = "high"
            pubMsg = client.publish(
                topic='rpi/purple',
                payload=msg,
                qos=0,
            )
            pubMsg.wait_for_publish()
            print(pubMsg.is_published())
            purple["hit_timer"] = curr
        except Exception as e:
            print(e)
        return{"state": "high"}
    else:
        return {"state": "cooldown"}


def shield():
    curr = time.time()
    if(curr - purple["shield_timer"] > shield_timer_delay):
        from mqtt_network.mqtt_cerelac import client
        try:
            msg = "shield"
            pubMsg = client.publish(
                topic='rpi/purple',
                payload=msg.encode('utf-8'),
                qos=0,
            )
            pubMsg.wait_for_publish()
            print(pubMsg.is_published())
            purple["shield_timer"] = curr
        except Exception as e:
            print(e)
        return{"state": "shield"}
    else:
        return {"state": "cooldown"}

def is_alive():
    curr = time.time()
    tmp = curr - purple["is_alive_timer"] 
    if(tmp > 6):
        purple["is_alive_timer"] = curr
        purple["is_alive"] = False
        return {"state": "not_connected"}
    purple["is_alive_timer"] = curr
    purple["is_alive"] = True
    return {"state": "connected"}

def disconnect():
    purple["is_alive_timer"] -= 7
    return {"purple": "not_connected"}