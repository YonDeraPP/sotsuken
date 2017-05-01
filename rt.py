import io
import picamera
import cv2

import numpy as np

stream = io.BytesIO()

CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)

for i in xrange(10):
        camera.capture(stream, format='jpeg')
        data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(data, 1)
        cv2.imshow('image',image)
        cv2.waitKey(16)
        stream.seek(0)
        print "captured %d" % (i)