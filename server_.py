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

HOST = "192.168.10.46"
PORT = 8000

stream = io.BytesIO()

camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH,CAMERA_HEIGHT)

def Capture():
    camera.capture(stream, format='jpeg')
    data = stream.getvalue()
    return data

class TCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        jpegstring = Capture()
        self.request.send(jpegstring)



if __name__ == '__main__':
    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.TCPServer((HOST, PORT), TCPHandler)

    print "start server"

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.shutdown()
    sys.exit()

