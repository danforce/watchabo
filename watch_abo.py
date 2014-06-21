from VideoCapture import Device
import os
import time

from flask import Flask
from flask.templating import render_template


app = Flask(__name__)
camera = Device(devnum=0)
last_capture = 0


@app.route('/')
def home():
    global last_capture
    capture_interval = 4
    if time.time() - last_capture > capture_interval:
        this_dir = os.path.dirname(__file__)
        image_file = os.path.join(this_dir, "static", "images", "test_image.jpg")
        camera.saveSnapshot(image_file, timestamp=3, boldfont=1)
        last_capture = time.time()
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
