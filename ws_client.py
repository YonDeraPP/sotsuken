# -*- coding:utf-8 -*-

from websocket import create_connection
import sys
import io
import picamera
import numpy as np
import base64

import cv2
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

stream = io.BytesIO()

camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH,CAMERA_HEIGHT)

def Capture():
    camera.capture(stream, format = 'jpeg')
    data = stream.getvalue()
    stream.seek(0)
    return data

if __name__ == '__main__':
    data = Capture()
    ws = create_connection("ws://192.168.10.54:8000/websocket")
    #data = "hello"
    print data[:4].decode('base64')
    ws.send(data.encode('base64'))

    print ws.recv()
    ws.close()