import RPi.GPIO as GPIO
import time


led_red = 14
led_yellow = 15
led_green = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_yellow, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)

def lights_off(led_red, led_yellow, led_green):
    GPIO.output(led_red, False)
    GPIO.output(led_yellow, False)
    GPIO.output(led_green, False)
    
def light_on(value):
    GPIO.output(value, True)

def light_off(value):
    GPIO.output(value, False)
    
lights_off(led_red, led_yellow, led_green)

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
