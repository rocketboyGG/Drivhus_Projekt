import smbus
import time

class MCP3021:
    bus = smbus.SMBus(1)
   
    def __init__(self, address = 0x48):
        self.address = address
   
    def read_raw(self):
        # Reads word (16 bits) as int
        rd = self.bus.read_word_data(self.address, 0)
        # Exchanges upper and lower bytes
        data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
        # Ignores two least significiant bits
        return data >> 2

    def fugt_procent(self):
        adc = self.read_raw()
        print("Fugt raw!", adc)
        procent = ((780-adc)/(780-308))*100
        if procent < 0:
            procent = 0
        return procent
"""
adc = MCP3021()

while True:
    raw = adc.read_raw()
    print("Raw :", raw)
    print("procent :", adc.fugt_procent())
    time.sleep(1)
"""
