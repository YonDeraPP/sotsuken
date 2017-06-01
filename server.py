#-*-coding:utf-8-*-

import cv2.cv as cv
import cv2
import numpy
import socket

if __name__ == "__main__":
    cv.NamedWindow("serverCAM", 1)  # 表示するウィンドウ作成

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("192.168.10.54", 12345))

    buff = 1024
    while True:
        jpgstring, addr = udp.recvfrom(buff*64)
        narray = numpy.fromstring(jpgstring, dtype=numpy.uint8)
        decimg = cv2.imdecode(narray, 1)

        cv2.imshow("serverCAM", decimg)
        if cv.WaitKey(10) == 27:
            break

    cv.DestroyAllWindows()
    udp.close()