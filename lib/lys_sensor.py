import smbus

class LysSensor:
    bus = smbus.SMBus(1)
    


    def __init__(self, address = 0x4B):
        self.address = address
        self.alpha = -0.06355932203
        self.beta = 65.02118644
   
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
        if blueDC > 77:
            blueDC = 77
        if redDC > 60:
            redDC = 60

        return int(redDC), int(blueDC)
    