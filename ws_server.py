# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.websocket

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
            print message
            # クライアントへメッセージを送信
            client.write_message(message)

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