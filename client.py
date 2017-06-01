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
    print len(data)
    stream.seek(0)
    return data


if __name__ == '__main__':
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        jpegstring = Capture()
        udp.sendto(jpegstring, (HOST,PORT))


    udp.close()
