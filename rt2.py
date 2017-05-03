#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import picamera
import cv2
import numpy as np
import io

cascade_path = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_path)

windowName = 'image'
cv2.namedWindow(windowName)
switch = True
color = (255,255,255)
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 12
    stream = io.BytesIO()

    while True:
        camera.capture(stream, format="jpeg", use_video_port=True)
        frame = np.fromstring(stream.getvalue(), dtype=np.uint8)
        stream.seek(0)
        frame = cv2.imdecode(frame, 1)

        image_gray = cv2.cvtColor(frame, cv2.cv.CV_BGR2GRAY)
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
        image_output = frame
        if len(facerect) > 0 and switch == True:
            for rect in facerect:
                cv2.rectangle(image_output, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)
                print "found"
            switch = False

        cv2.imshow(windowName, frame)

        key = cv2.waitKey(33)
        if key == 1048603:
            break

cv2.destroyAllWindows()