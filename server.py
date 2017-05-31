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

def getimage():
        soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        soc.connect(('192.168.10.46',8000))
        soc.send('HELLO\n')
        buf = ' '
        recvlen = 100
        while recvlen>0:
            receivedstr=soc.recv(1024*8)
            recvlen=len(receivedstr)
            buf +=receivedstr
        soc.close()
        
        narray = np.fromstring(buf,dtype=np.uint8)
        
        img = cv2.imdecode(narray,1)
        
        return img

if __name__ == '__main__':
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((HOST,PORT))

        while True:
                s.listen(1)
                soc, addr = s.accept()
                print "Connected by " , addr
                soc.send("HELLO\n")
                buf = ' '
                recvlen=100
                while recvlen>50:
                    receivedstr=soc.recv(1024*8)
                    recvlen=len(receivedstr)
                    buf += receivedstr
                    print recvlen
                soc.close()
                
                print "socket closed"
                
                narray = np.fromstring(buf,dtype=np.uint8)
                img = cv2.imdecode(narray,1)
                
                cv2.imshow("capture",img)

                if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                
