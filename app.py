from flask import Flask, render_template, redirect, url_for
from lib.camera import Camera
from lib.fugt_sensor import FugtSensor
from sqlite3 import Connection
import base64
from io import BytesIO
from matplotlib.figure import Figure


app = Flask(__name__)
cam = Camera()
fugt_sen = FugtSensor()

fugt_sen.insert_soilmoisture()

def select_images(amount):
    if isinstance(amount, int) and amount > 0:
        con = Connection("drivhus.db")
        cur = con.cursor()
        sql = f"""SELECT Timestamp FROM Images ORDER BY rowid DESC LIMIT {amount}"""
        cur.execute(sql)
        img_rows = cur.fetchall()
        print(img_rows)
        con.close()
        return img_rows

@app.route("/")
def home():
    soil_data = fugt_sen.select_soil_percentage(10)
    fig = Figure()
    ax = fig.subplots()
    x = []
    y = []
    ax.tick_params(axis='x', which='both', rotation=30)
    fig.subplots_adjust(bottom=0.3)
    ax.set_xlabel("Timestamps")
    ax.set_ylabel("Soilmoisture %")
    for row in soil_data:
        x.append(row[1])
        y.append(row[0])
    ax.plot(x, y)
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template("home.html", soil_data = data)

@app.route("/plant_pic/")
def plant_pic():
    cam.capture_pic()
    return render_template("plant_pic.html", image = select_images(1)[0][0])

@app.route("/gallery/")
def gallery():
    image_rows = select_images(12)
    return render_template("gallery.html", image_rows = image_rows)

if __name__ == ('__main__'):
    app.run(host="0.0.0.0", debug=True)
