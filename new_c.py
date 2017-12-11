import time

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

def Capture():
    camera.capture('image.jpg')
    data = open("image.jpg","rb")
    return data


url = 'http://192.168.10.8:8000/'
while True:
    print("hello")
    data = Capture()
    files = {'upload': data}
    res = requests.post(url, files=files)
    print(res)
    time.sleep(60*60)