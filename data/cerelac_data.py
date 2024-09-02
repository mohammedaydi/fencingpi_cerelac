import RPi.GPIO as gpio_tmp

is_available = True
is_moving = False
entry_pass = "we15"
users = [{"username": "mohammedaydi",
          "password": "159"}]

purple = {"is_alive": False, "hp": 100,"is_alive_timer": 0,"hit_timer": 0,"shield_timer": 0,"position" : 10}

black = {"is_alive": True, "hp": 100,"is_alive_timer": 0,"hit_timer": 0,"shield_timer": 0,"position" : 10} 


gpio = gpio_tmp
enPin = 11
stepPin = 10
directionPin = 9
purple_front_switch = 20
purple_rear_switch = 21

enPin2 = 27
stepPin2 = 22
directionPin2 = 17
black_front_switch = 12
black_rear_switch = 16

def initialize_gpios():
    gpio.cleanup()
    gpio.setmode(gpio.BCM)
    gpio.setup(enPin,gpio.OUT)
    gpio.setup(directionPin,gpio.OUT)
    gpio.setup(stepPin,gpio.OUT)
    gpio.setup(purple_front_switch,gpio.IN)
    gpio.setup(purple_rear_switch,gpio.IN)
    gpio.output(enPin,gpio.LOW)

    gpio.setup(enPin2,gpio.OUT)
    gpio.setup(directionPin2,gpio.OUT)
    gpio.setup(stepPin2,gpio.OUT)
    gpio.setup(black_front_switch,gpio.IN)
    gpio.setup(black_rear_switch,gpio.IN)
    gpio.output(enPin2,gpio.LOW)