# -*-coding:utf-8-*-

import requests
import json
import picamera
import io
import base64

CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240
stream = io.BytesIO()

camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH,CAMERA_HEIGHT)

def Capture():
    camera.capture(stream, format='jpeg')
    data = stream.getvalue()
    stream.seek(0)
    return data


url = 'http://192.168.10.54:5000/'
files = base64.b64encode(Capture())

res = requests.post(url, data = files[:8])

print(res)
