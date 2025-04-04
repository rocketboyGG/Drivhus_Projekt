from time import sleep
from lib.led_light import LED_sun
from lib.pumpe import Pumpe
from lib.Fugt import MCP3021

pumpe = Pumpe(16)
led_sun = LED_sun(12, 13)   
fugt_sensor = MCP3021()

led_sun.set_duty_RED(60)
led_sun.set_duty_BLUE(77)

while True:
    procent = fugt_sensor.fugt_procent()
    if procent < 10:
        pumpe.turnOn()
    elif procent > 60:
        pumpe.turnOff()
    sleep(3)
