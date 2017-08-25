#-*- coding:utf-8 -*-
import picamera
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH,CAMERA_HEIGHT)
def Capture():
    camera.capture('image_.jpg')
    return 'hello'

Capture()