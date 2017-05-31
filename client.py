#-*-coding:utf-8-*-

import socket
import numpy as np
import io

import picamera

CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

HOST = '192.168.10.54'
PORT = 8000

stream = io.BytesIO()

camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH,CAMERA_HEIGHT)

def Capture():
    camera.capture(stream, format = 'jpeg')
    data = stream.getvalue()
    stream.seek(0)
    return data


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    i = 0
    print "Connected to ",HOST
    while True:
        data = s.recv(1024).strip()
        s.send(Capture())
        
    s.close()
    
