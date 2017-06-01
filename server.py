#-*-coding:utf-8-*-

import cv2.cv as cv
import cv2
import numpy
import socket

if __name__ == "__main__":
    cv.NamedWindow("serverCAM", 1)  # 表示するウィンドウ作成

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("192.168.10.52", 8000))

    buff = 1024
    while True:
        jpgstring, addr = udp.recvfrom(buff * 64)  # 送られてくるデータが大きいので一度に受け取るデータ量を大きく設定
        narray = numpy.fromstring(jpgstring, dtype="uint8")  # string型からnumpyを用いuint8に戻す
        decimg = cv2.imdecode(narray, 1)  # uint8のデータを画像データに戻す

        cv2.imshow("serverCAM", decimg)
        if cv.WaitKey(10) == 27:
            break

    cv.DestroyAllWindows()
    udp.close()