# -*- coding: utf-8 -*-
import io
import picamera
import cv2

import numpy as np


with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 24
    stream = io.BytesIO()

    while True:
        camera.capture(stream, format="jpeg", use_video_port=True)
        frame = np.fromstring(stream.getvalue(), dtype=np.uint8)
        stream.seek(0)
        frame = cv2.imdecode(frame, 1)

        cv2.imshow('capture',frame)


    cv2.destroyAllWindows()