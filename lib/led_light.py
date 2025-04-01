import pigpio # (1)
from time import sleep

# LED_RED = 12 & LED_BLUE 13
# RED DUTY 60% & BLUE 77%

class LED_sun:
    def __init__(self, LED_RED, LED_BLUE):
        pi = pigpio.pi()
        self.LED_RED = LED_RED
        self.LED_BLUE = LED_BLUE
        self.pi = pigpio.pi()
        self.pi.set_PWM_range(self.LED_RED, 100)
        self.pi.set_PWM_range(self.LED_BLUE, 100)
        self.pi.set_PWM_frequency(self.LED_RED, 100000)
        self.pi.set_PWM_frequency(self.LED_BLUE, 100000)

    def set_duty_RED(self, duty):
        self.pi.set_PWM_dutycycle(self.LED_RED, duty)

    def set_duty_BLUE(self, duty):
        self.pi.set_PWM_dutycycle(self.LED_BLUE, duty)

    def print_duty(self):
        print(f"RED duty", {self.pi.get_PWM_dutycycle(self.LED_RED)}, "BLUE duty", {self.pi.get_PWM_dutycycle(self.LED_BLUE)})
