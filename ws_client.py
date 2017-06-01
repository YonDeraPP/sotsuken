# -*- coding:utf-8 -*-

from websocket import create_connection
import sys
import io
import picamera
import numpy as np

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
    ws = create_connection("ws://localhost:8000/websocket")
    data = Capture()
    print type(data)
    ws.send(data)

    ##data = ws.recv()
    #narray = np.fromstring(data,dtype=np.uint8)
    #img = cv2.imdecode(narray,1)
   # cv2.imshow("capture",img)
    print ws.recv()

    ws.close()