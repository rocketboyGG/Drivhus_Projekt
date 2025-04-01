import pigpio
from time import sleep

# PIN PUMPE 36

class Pumpe:
    def __init__(self, pin):
        self.pin = pin
        self.pi = pigpio.pi()
        self.pi.set_mode(self.pin, pigpio.OUTPUT)
    
    def turnOn(self):
        self.pi.write(self.pin, 1)
        print("Pumpe pin værdi: ",self.pi.read(self.pin))
    
    def turnOff(self):
        self.pi.write(self.pin, 0)
        print("Pumpe pin værdi: ",self.pi.read(self.pin))

        
        
        
