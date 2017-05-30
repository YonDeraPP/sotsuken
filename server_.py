#-*-coding:utf-8-*-

import SocketServer
import cv2
import numpy  as np
import socket
import sys

import io
import picamera
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

stream = io.BytesIO()

camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH,CAMERA_HEIGHT)

def capture():
    data = stream.getvalue()
    return type(data)

if __name__ == '__main__':
    while True:
        print capture()