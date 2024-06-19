from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import led_control
#Empty list to store sequence of keypad presses
password = []

lcd = LCD.lcd()
lcd.lcd_clear()

#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    password.append(key)
    lcd = LCD.lcd()
    if key == 0:
        led_control.led_control_init(0)
        lcd.lcd_clear
        lcd.lcd_display_string("LED CONTROL",1)
        lcd.lcd_display_string("OFF LED",2)
    elif key == 1:
        led_control.led_control_init(1)
        lcd.lcd_clear
        lcd.lcd_display_string("LED CONTROL",1)
        lcd.lcd_display_string("BLINK LED",2)
    print(password)


def main():
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()

    # Display something on LCD
    lcd.lcd_display_string("LED Control", 1)
    lcd.lcd_display_string("0:OFF 1:BLINK",2)

    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    led_control.led_control_init(0)



# Main entry point
if __name__ == "__main__":
    main()


