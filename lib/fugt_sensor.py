import smbus
import time
import threading
from datetime import datetime
from sqlite3 import Connection

class FugtSensor:
    bus = smbus.SMBus(1)
   
    def __init__(self, address = 0x48):
        self.address = address
   
    def read_raw(self, addr):
        # Reads word (16 bits) as int
        rd = self.bus.read_word_data(addr, 0)
        # Exchanges upper and lower bytes
        data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
        # Ignores two least significiant bits
        return data >> 2

    def fugt_procent(self):
        adc = self.read_raw(0x48)
        procent = ((780-adc)/(780-308))*100
        data = round(procent, 2)
        if data < 0:
            data = 0
        return data
    
    def insert_soilmoisture(self):
        date_time = datetime.now()
        timestamp = f"{date_time.strftime('%d-%m-%Y-%H:%M:%S')}"
        con = Connection("drivhus.db")
        cur = con.cursor()
        moisture_percentage = self.fugt_procent()
        params = (timestamp, moisture_percentage)
        sql = """INSERT INTO SoilMoisture (Timestamp, moisture_percentage) VALUES(?, ?)"""
        cur.execute(sql, params)
        con.commit()
        con.close()
    
    def continous_measure(self):
        while True:
            self.soil_moisture_percent = self.fugt_procent()
            sleep(0.2)
        
    def start_continous_measure(self):
        soil_thread = threading.Thread(target=self.continous_measure)
        soil_thread.start()

    def select_soil_percentage(self, amount):
        if isinstance(amount, int) and amount > 0:
            con = Connection("drivhus.db")
            cur = con.cursor()
            sql = f"""SELECT moisture_percentage, Timestamp FROM SoilMoisture ORDER BY rowid DESC LIMIT {amount}"""
            cur.execute(sql)
            img_rows = cur.fetchall()
            print(img_rows)
            con.close()
            return img_rows




