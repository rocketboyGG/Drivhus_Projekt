from time import sleep, time
from lib.led_light import LED_sun
from lib.pumpe import Pumpe
from lib.fugt_sensor import MCP3021
from lib.lys_sensor import LysSensor
import schedule

pumpe = Pumpe(16)
led_sun = LED_sun(12, 13)   
fugt_sensor = MCP3021()
lys_sen = LysSensor()

led_sun.set_duty_RED(60)
led_sun.set_duty_BLUE(77)

fugt_time = time()

def fugtcheck():
    print("checker fugt!")
    if procent < 60:
        print("tænder pumpe!")
        pumpe.turnOn()
        sleep(2)
        pumpe.turnOff()

schedule.every(1).minutes.do(fugtcheck)

while True:
    procent = fugt_sensor.fugt_procent()
    print("Fugt Procent", procent)
    print("Lys ", lys_sen.read_raw())
    """
    if time() - fugt_time >= 10:
        if procent < 60:
            pumpe.turnOn()
            sleep(2)
            pumpe.turnOff()
            """
    schedule.run_pending()
    sleep(3)