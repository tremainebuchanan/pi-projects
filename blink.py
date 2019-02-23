import RPi.GPIO as GPIO
import time

led_blue = 18
led_red = 2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_blue, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)

while True:
    GPIO.output(led_blue, True) #blue on
    time.sleep(1)
    GPIO.output(led_blue, False) #blue off
    time.sleep(1)
    GPIO.output(led_red, True) #red on
    time.sleep(1)
    GPIO.output(led_red, False) #red off