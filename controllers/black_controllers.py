import time
from data.cerelac_data import black
import RPi.GPIO as gpio


enPin = 27
stepPin = 22
directionPin = 17
is_initial = True

hit_timer_delay = 4
shield_timer_delay = 3

def setup_pins():
    gpio.setmode(gpio.BCM)
    gpio.setup(enPin,gpio.OUT)
    gpio.setup(directionPin,gpio.OUT)
    gpio.setup(stepPin,gpio.OUT)
    gpio.output(enPin,gpio.LOW)
    is_initial = False

def move_forward2():
    if is_initial:
        setup_pins()

    gpio.output(directionPin,gpio.HIGH)
    time.sleep(0.01)
    for x in range(0,1600):
        gpio.output(stepPin,gpio.HIGH)
        time.sleep(0.000600)
        gpio.output(stepPin,gpio.LOW)
        time.sleep(0.000600)
    gpio.cleanup()
    return {"state": "moved_forward"}

def move_backwards2():
    if is_initial:
        setup_pins()
    gpio.output(directionPin,gpio.LOW)
    time.sleep(0.01)
    for x in range(0,1600):
        gpio.output(stepPin,gpio.HIGH)
        time.sleep(0.000600)
        gpio.output(stepPin,gpio.LOW)
        time.sleep(0.000600)
    gpio.cleanup()
    return {"state": "moved_backward"}

def rotate_right2():
    curr = time.time()
    if(curr - black["hit_timer"] > hit_timer_delay):
        from mqtt_network.mqtt_cerelac import client
        try:
            msg = "side"
            pubMsg = client.publish(
                topic='rpi/black',
                payload=msg.encode('utf-8'),
                qos=0,
            )
            pubMsg.wait_for_publish()
            print(pubMsg.is_published())
            black["hit_timer"] = curr
        except Exception as e:
            print(e)
        return{"state": "side"}
    else:
        return {"state": "cooldown"}



def rotate_left2():
    curr = time.time()
    if(curr - black["hit_timer"] > hit_timer_delay):
        from mqtt_network.mqtt_cerelac import client
        try:
            msg = "defend"
            pubMsg = client.publish(
                topic='rpi/black',
                payload=msg.encode('utf-8'),
                qos=0,
            )
            pubMsg.wait_for_publish()
            print(pubMsg.is_published())
            black["hit_timer"] = curr
        except Exception as e:
            print(e)
        return{"state": "defend"}
    else:
        return {"state": "cooldown"}


def high2():
    curr = time.time()
    if(curr - black["hit_timer"] > hit_timer_delay):
        from mqtt_network.mqtt_cerelac import client
        try:
            msg = "high"
            pubMsg = client.publish(
                topic='rpi/black',
                payload=msg.encode('utf-8'),
                qos=0,
            )
            pubMsg.wait_for_publish()
            print(pubMsg.is_published())
            black["hit_timer"] = curr
        except Exception as e:
            print(e)
        return{"state": "high"}
    else:
        return {"state": "cooldown"}

def shield2():
    curr = time.time()
    if(curr - black["shield_timer"] > shield_timer_delay):
        from mqtt_network.mqtt_cerelac import client
        try:
            msg = "shield"
            pubMsg = client.publish(
                topic='rpi/black',
                payload=msg.encode('utf-8'),
                qos=0,
            )
            pubMsg.wait_for_publish()
            print(pubMsg.is_published())
            black["shield_timer"] = curr
        except Exception as e:
            print(e)
        return{"state": "shield"}
    else:
        return {"state": "cooldown"}



def is_alive():
    curr = time.time()
    tmp = curr - black["is_alive_timer"] 
    if(tmp > 6):
        black["is_alive_timer"] = curr
        black["is_alive"] = False
        return {"state": "not_connected"}
    black["is_alive_timer"] = curr
    black["is_alive"] = True
    return {"state": "connected"}

def disconnect():
    black["is_alive_timer"] -= 7
    return {"black": "not_connected"}