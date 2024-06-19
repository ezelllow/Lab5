import time
from time import sleep
from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import hal.hal_buzzer as buzzer
import RPi.GPIO as GPIO

incorrect_attempts = 0

password = [1,2,3,4]
pin = []

lcd = LCD.lcd()
lcd.lcd_clear()

def update_lcd_with_masked_pin():
    masked_pin = '*' * len(pin)
    lcd.lcd_clear()  # Clear entire LCD
    lcd.lcd_display_string("Safe Lock", 1)
    lcd.lcd_display_string(masked_pin, 2)
    
def check_pin():
    global incorrect_attempts
    if pin == password:
        lcd.lcd_clear()
        lcd.lcd_display_string("Safe Unlock", 1)
        lcd.lcd_display_string("“”", 2)
    else:
        incorrect_attempts += 1
        GPIO.output(18, 1)  # Turn on the buzzer
        time.sleep(1)  # Duration to turn on the buzzer
        GPIO.output(18, 0)  # Turn off when time is up
        lcd.lcd_clear()
        lcd.lcd_display_string("Wrong Pin", 1)
        lcd.lcd_display_string("“”", 2)
        update_lcd_with_masked_pin()

        if incorrect_attempts >= 3:
            lcd.lcd_clear()
            lcd.lcd_display_string("Safe Disabled", 1)
            lcd.lcd_display_string("“”", 2)
            pin.clear()  # Clear current pin entry
            keypad.disable()  # Disable keypad input

def key_pressed(key):
    pin.append(key)
    update_lcd_with_masked_pin()

    if len(pin) == 4:
        check_pin()
        if pin != password:
            pin.clear()
            lcd.lcd_clear()
            lcd.lcd_display_string("Safe Lock", 1)
            lcd.lcd_display_string("Enter Pin", 2)
        

def main():

    GPIO.setmode(GPIO.BCM)  # choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)  # set GPIO 18 as output

    lcd.lcd_display_string("Safe Lock", 1)
    lcd.lcd_display_string("Enter Pin", 2)

    keypad.init(key_pressed)

    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

if __name__ == "__main__":
    main()
