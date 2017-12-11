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
    camera.capture('image.jpg')
    data = open("image.jpg","rb")
    return data


url = 'http://192.168.10.63:8000/'

@app.route('/')
def index():
    print("hello")
    data = Capture()
    files = {'upload': data}
    res = requests.post(url, files=files)
    print(res)
    url2 = url + 'empty'
    res = requests.get(url2)
    print(res)
    return 'hello'

@app.route('/empty')
def empty():
    data = {'message':datetime.datetime.today()}
    res = requests.post(url,data = json.dumps(data))

if __name__ == '__main__':
    app.run(host="0.0.0.0")