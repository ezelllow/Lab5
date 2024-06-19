import hal.hal_servo as servo
import hal.hal_adc as adc

def main():
    servo.init()
    adc.init()
    while(True):
        pot = adc.get_adc_value(0)

        servo.set_servo_position(180-(pot/1023 * 180))

if __name__ == "__main__":
    main()