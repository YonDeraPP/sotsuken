from flask import Flask

import requests
import json
import picamera
import io
import base64
import datetime

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
stream = io.BytesIO()

camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH,CAMERA_HEIGHT)
app = Flask(__name__)

def Capture():
    today = datetime.datetime.today()
    camera.capture('image_.jpg')
    return 'hello'


url = 'http://192.168.10.63:8000/'

@app.route('/')
def index():
    print("hello")
    return Capture()

@app.route('/empty')
def empty():
    data = {'message':datetime.datetime.today()}
    res = requests.post(url,data = json.dumps(data))

<<<<<<< HEAD
if __name__ == '__main__':
    app.run(host="0.0.0.0")
=======

app.run(host="0.0.0.0",port = 5000)
>>>>>>> 5086e1f575be172308603d778936fe027647dbc5
