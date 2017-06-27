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
    camera.capture('image.jpg')
    data = open("image.jpg","rb")
    return data


url = 'http://192.168.10.54:5000/'
files = {'upload':data}

res = requests.post(url, files = files)

print(res)
