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
    camera.capture(today.strftime("%Y%m%d-%H%M")+'.jpg')
    data = open(today.strftime("%Y%m%d-%H%M")+'.jpg',"rb")
    return data


url = 'http://192.168.10.63:8000/'

@app.route('/')
def index():
    print("hello")
    data = Capture()
    return 'hello'

@app.route('/empty')
def empty():
    data = {'message':datetime.datetime.today()}
    res = requests.post(url,data = json.dumps(data))


app.run(host="0.0.0.0",port = 5000)