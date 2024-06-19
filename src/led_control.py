import RPi.GPIO as GPIO #import RPi.GPIO module
from hal import hal_led as led
from threading import Thread
from time import sleep

from hal import hal_keypad as keypad

def init():
    GPIO.setmode(GPIO.BCM)  # choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(24, GPIO.OUT)  # set GPIO 24 as output
    
def led_thread():
    global delay

    while(True):
        if delay != 0:
            led.set_output(24,1)
            sleep(delay)
            
            led.set_output(24, 0)
            sleep(delay)    

def led_control_init(delay_input):
    led.init()
    global delay
    delay = delay_input
    t1 = Thread(target=led_thread)
    t1.start()
    #Set initial LED blinking every 1 second after Thread starts