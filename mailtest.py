# -*- coding: utf-8 -*-
import picamera
import io
import numpy as np
import cv2

stream = io.BytesIO()

cascade_path = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_path)

CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

color = (255,255,255)
camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)

def main():
    while True:
        camera.capture(stream,format='jpeg')
        data = np.fromstring(stream.getvalue(),dtype=np.uint8)
        image = cv2.imdecode(data,1)

        image_gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

        if len(facerect)>0:
            print 'detected'

        cv2.imshow('image',image)
        cv2.waitKey(0)
        stream.seek(0)


if __name__ == '__main__':
    main()