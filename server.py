#-*-coding:utf-8-*-
import io
import cv2

import numpy as np

import socket

stream = io.BytesIO()

CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

HOST = '192.168.10.54'
PORT = 8000

def getimage(data):
        narray = np.fromstring(data,dtype=np.uint8)
        
        img = cv2.imdecode(narray,1)
        
        return narray

if __name__ == '__main__':
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((HOST,PORT))
        s.listen(1)
        soc, addr = s.accept()
        print "Connected by " , addr

        while True:
                data = soc.recv(320*240)
                img = getimage(data)
                pic = cv2.imdecode(img,1)
                cv2.imshow("capture",pic)

                if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                
