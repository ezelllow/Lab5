import time
from time import sleep
from threading import Thread
from hal import hal_lcd as LCD

lcd = LCD.lcd()
lcd.lcd_clear()

def get_current_time_and_date():
    local_time = time.localtime()
    time_string = time.strftime("%H:%M:%S", local_time)
    date_string = time.strftime("%d:%m:%Y", local_time)
    return time_string, date_string

def blink_colon():
    while True:
        time_string, date_string = get_current_time_and_date()
        
        # Display time without the colon
        lcd.lcd_display_string(f"Time: {time_string[:2]} {time_string[3:5]} {time_string[6:8]}", 1)#3:5 means 3-4, :2 means 0-1
        lcd.lcd_display_string(f"Date: {date_string}", 2)
        sleep(1)
        
        # Display time with the colon
        lcd.lcd_display_string(f"Time: {time_string}", 1)
        lcd.lcd_display_string(f"Date: {date_string}", 2)
        sleep(1)

def main():
    # Start the blink colon thread
    blink_thread = Thread(target=blink_colon)
    blink_thread.start()

if __name__ == "__main__":
    main()

