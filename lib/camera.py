from picamera2 import Picamera2, Preview
from datetime import datetime
from sqlite3 import Connection

class Camera:
    def __init__(self):
        pass
        #self.picam2 = Picamera2()
        

    def capture_pic(self):
        date_time = datetime.now()
        datetime_img = f"{date_time.strftime('%d-%m-%Y-%H:%M:%S')}.jpg"
        picam2 = Picamera2()
        config = picam2.create_preview_configuration(main={"size": (640, 480)})
        #config["transform"] = libcamera.Transform(hflip=1, vflip=1)
        picam2.configure(config)
        picam2.start_preview(Preview.NULL)
        picam2.start()
        picam2.capture_file(f"static/img/{datetime_img}")
        picam2.close()
        self.insert_img(datetime_img)

    def insert_img(self, timestamp):
        con = Connection('drivhus.db')
        cur = con.cursor()
        params = (timestamp,)
        sql = """ INSERT INTO Images (Timestamp) VALUES(?) """
        cur.execute(sql, params)
        con.commit()
        con.close()