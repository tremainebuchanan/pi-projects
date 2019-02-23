'Stop Light program using Raspberry Pi'
'Author: Tremaine Buchanan'
import RPi.GPIO as GPIO
import time

led_red = 14 # Assign red LED to GPIO 14
led_yellow = 15 # Assign yellow LED to GPIO 15 
led_green = 18 # Assign green LED to GPIO 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_yellow, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)

'Ensures the stoplight starts at red once turned on'
def reset(led_red, led_yellow, led_green):
    GPIO.output(led_red, False)
    GPIO.output(led_yellow, False)
    GPIO.output(led_green, False)

'Turns on a specific LED'
def light_on(value):
    GPIO.output(value, True)
    
'Turns off a specific LED'
def light_off(value):
    GPIO.output(value, False)
    
reset(led_red, led_yellow, led_green)

while True:
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
