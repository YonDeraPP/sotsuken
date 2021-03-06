# -*-coding:utf-8-*-

import requests
import json
import picamera
import io
import base64
import RPi.GPIO as GPIO

CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240
stream = io.BytesIO()

camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH,CAMERA_HEIGHT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

def Capture():
    camera.capture('image.jpg')
    data = open("image.jpg","rb")
    return data


url = 'http://192.168.10.63:8000/'

if __name__ == '__main__':
    try:
        while True:
            if GPIO.input(18):
                data = Capture()
                files = {'upload':data}
                res = requests.post(url, files = files)
                print(res)
    except KeyboardInterrupt:
        pass