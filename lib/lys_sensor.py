import smbus

class LysSensor:
    bus = smbus.SMBus(1)

    def __init__(self, address = 0x4B):
        self.address = address
   
    def read_raw(self):
        # Reads word (16 bits) as int
        rd = self.bus.read_word_data(self.address, 0)
        # Exchanges upper and lower bytes
        data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
        # Ignores two least significiant bits
        return data >> 2

    def brightnessToDutyCycles(self):
        adcVal = self.read_raw()
        redDC = self.alpha * adcVal + self.beta
        blueDC = redDC * 77 / 60
        return redDC, blueDC