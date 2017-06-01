# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.websocket
import cv2
import numpy as np

cascade_path = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_path)

cl = []


# クライアントからメッセージを受けるとopen → on_message → on_closeが起動する
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    # websocketオープン
    def open(self):
        print "open"
        if self not in cl:
            cl.append(self)

    # 処理
    def on_message(self, message):
        print "on_message"
        for client in cl:
            print message[:4]
            data = np.fromstring(message.decode('base64'),dtype=np.uint8)
            img = cv2.imdecode(data,1)
            image_gray = cv2.cvtColor(img, cv2.cv.CV_BGR2GRAY)
            facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1,minSize=(1,1))
            if len(facerect) > 0:
                client.write_message("found!")
                print "found"
            else:
                client.write_message("Not found!")
                print "Not found"

    # websockeクローズ
    def on_close(self):
        print "close"
        if self in cl:
            cl.remove(self)


app = tornado.web.Application([
    (r"/websocket", WebSocketHandler)
])

if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()