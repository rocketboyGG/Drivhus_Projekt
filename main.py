from time import sleep
from lib.led_light import LED_sun
from lib.pumpe import Pumpe

pumpe = Pumpe(14)
led_sun = LED_sun(12, 13)

led_sun.set_duty_RED(60)
led_sun.set_duty_RED(77)

while True:
    led_sun.print_duty()
    pumpe.turnOn()
    sleep(1)
    pumpe.turnOff()