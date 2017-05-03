#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import picamera
import io

camera = picamera.PiCamera()
camera.resolution = (1024, 768)
time.sleep(2) #カメラ初期化
stream = io.BytesIO()

for foo in camera.capture_continuous(stream, "jpeg", use_video_port=True):
    stream.seek(0)
    frame = stream.getvalue() #これで１フレーム取り出せる
    stream.seek(0)
    stream.truncate()