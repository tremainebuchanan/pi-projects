'Stop Light program using Raspberry Pi'
'Author: Tremaine Buchanan'
import RPi.GPIO as GPIO
import time
import subprocess
import random

led_red = 14 # Assign red LED to GPIO 14
led_yellow = 15 # Assign yellow LED to GPIO 15 
led_green = 18 # Assign green LED to GPIO 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_yellow, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
lights = {14: "red", 15: "yellow", 18: "green"}
led_list = [14, 15, 18]

'Ensures the stoplight starts at red once turned on'
def reset(led_red, led_yellow, led_green):
    GPIO.output(led_red, False)
    GPIO.output(led_yellow, False)
    GPIO.output(led_green, False)

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
reset(led_red, led_yellow, led_green)
log("Starting up...")
is_connected()
try:
    while True:
        print(random.randint(14,18))
        light_on(led_red)
        time.sleep(3)
        light_off(led_red)
        time.sleep(.1)
        light_on(led_green)
        time.sleep(3)
        light_off(led_green)
        time.sleep(.1)
        light_on(led_yellow)
        time.sleep(3)
        light_off(led_yellow)
        time.sleep(.1)
except KeyboardInterrupt:
    print("\nInterrupt received...Exiting...")
finally:
    reset(14, 15, 18)
'Program ends here'