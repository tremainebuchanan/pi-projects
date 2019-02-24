'Stop Light program using Raspberry Pi'
'Author: Tremaine Buchanan'
import RPi.GPIO as GPIO
import time
import subprocess
import random
from random import seed
from random import choice
#from random import shuffle

""" Callback Function Definitions """
def button_cb(channel):
    if not GPIO.input(player_one_led) == 0:
        light_off(23)
        time.sleep(.01)
        print("Button pressed")
        reset(14,15,18,23)
    
seed(1)
led_red = 14 # Assign red LED to GPIO 14
led_yellow = 15 # Assign yellow LED to GPIO 15 
led_green = 18 # Assign green LED to GPIO 18
player_one = 2
player_one_led = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_yellow, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(player_one_led, GPIO.OUT)
GPIO.setup(player_one, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.add_event_detect(player_one, GPIO.BOTH, callback=button_cb, bouncetime=300)
lights = {14: "red", 15: "yellow", 18: "green", 23: "player_one"}
led_list = [14, 15, 18, 23]
random_list = []
last_selected = 0
interval = 1

    
'Ensures the stoplight starts at red once turned on'
def reset(led_red, led_yellow, led_green, player_one_led):
    GPIO.output(led_red, False)
    GPIO.output(led_yellow, False)
    GPIO.output(led_green, False)
    GPIO.output(player_one_led, False)
    print("Game Reset")

'Turns on a specific LED'
def light_on(value):
    GPIO.output(value, True)
    message = lights.get(value)
    print(message + " light on")
    
'Turns off a specific LED'
def light_off(value):
    GPIO.output(value, False)
    message = lights.get(value)
    print(message + " light off")

   
'Print log message to console'
def log(message):
    print(message)

def get_unique_number(last_selected, led_list):
    selected = choice(led_list)
    while selected == last_selected:
        selected = choice(led_list)
    return selected
        

'Detect if the pi is connected to a network'
def is_connected():    
    ps = subprocess.Popen(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    try:
        output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout)
        if output:
            print('Connected')
    except subprocess.CalledProcessError:
        # grep did not match any lines
        print("No internet connection")

'Program starts here'
reset(led_red, led_yellow, led_green, player_one_led)
log("Starting up...")
is_connected()
try:
    while True:
        selection = get_unique_number(last_selected, led_list)
        if selection not in random_list and selection in lights:
            random_list.append(selection)
            if len(random_list) == 1:
                last_selected = 0 #reset last_selected such that it wont prevent the program from stalling
            light_on(selection)
            time.sleep(interval)
            light_off(selection)
            time.sleep(interval)
            print(random_list)
            if len(random_list) == 4:
                last_selected = random_list.pop(3)
                while len(random_list) > 0: random_list.pop()
            
except KeyboardInterrupt:
    print("\nInterrupt received...Exiting...")
finally:
    reset(14, 15, 18, 23)
    GPIO.cleanup()

GPIO.cleanup()
'Program ends here'
