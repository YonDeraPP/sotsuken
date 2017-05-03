#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import picamera
import cv2

import numpy as np

cascade_path = "/usr/share/opencv/haarcascades/haarcascade_fullbody.xml"
cascade = cv2.CascadeClassifier(cascade_path)

stream = io.BytesIO()

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)
color = (255, 255, 255)
camera.framerate = 24

print "Type Ctrl+C to Stop"

if __name__ == "__main__":
    while True:
            #picamera to opencv
            camera.capture(stream, format='jpeg',use_video_port=True)
            data = np.fromstring(stream.getvalue(), dtype=np.uint8)
            image = cv2.imdecode(data, 1)

            image_gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
            facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

            image_output = image
            if len(facerect)>0:
                for rect in facerect:
                    cv2.rectangle(image_output, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)
                    print "found"


            cv2.imshow('image',image)
            cv2.waitKey(16)
            stream.seek(0)
