from time import sleep, time
from lib.led_light import LED_sun
from lib.pumpe import Pumpe
from lib.fugt_sensor import FugtSensor
from lib.lys_sensor import LysSensor
from lib.camera import Camera
import schedule

pumpe = Pumpe(16)
led_sun = LED_sun(12, 13)   
fugt_sensor = FugtSensor()
lys_sen = LysSensor()
camera = Camera()



def fugtcheck():
    print("checker fugt!")
    if procent < 60:
        print("tænder pumpe!")
        pumpe.turnOn()
        sleep(2)
        pumpe.turnOff()

def morgen():
    ...

def nat():
    led_sun.set_duty_RED(0)
    led_sun.set_duty_BLUE(0)


schedule.every(100).minutes.do(fugtcheck)
schedule.every().day.at("08:00").do()
schedule.every().day.at("23:59").do(nat)
camera.capture_pic()

while True:
    procent = fugt_sensor.fugt_procent()
    print("Fugt Procent", procent)
    print("Lys ", lys_sen.read_raw())
    redDutyCycle, blueDutyCycle = lys_sen.brightnessToDutyCycles()
    print("Red Duty: ", redDutyCycle,"Blue Duty:",blueDutyCycle)
    led_sun.set_duty_RED(redDutyCycle)
    led_sun.set_duty_BLUE(blueDutyCycle)
    schedule.run_pending()
    sleep(3)