#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import picamera
import io
import  numpy as np
import cv2

camera = picamera.PiCamera()
camera.resolution = (1024, 768)
time.sleep(2) #カメラ初期化
stream = io.BytesIO()

for foo in camera.capture_continuous(stream, "jpeg", use_video_port=True):
    stream.seek(0)
    frame = np.fromstring(stream.getvalue(), dtype=np.uint8)
    data = cv2.imdecode(frame, 1)
    cv2.imshow('image',data)
    stream.seek(0)
    stream.truncate()