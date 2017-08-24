# -*-coding:utf-8-*-

from flask import Flask
from flask import request

import json
import cv2
import math
import os
import numpy as np

import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

app = Flask(__name__)


class sendGmail:
    jsonData = json.load(open('address.json', 'r'))
    username, password = jsonData['username'], jsonData['Password']

    def __init__(self, to, sub, body, mime=None, attach_file=None):
        host, port = 'smtp.gmail.com', 465
        to = to
        sub = sub
        bosy = body
        mime = mime
        attach_file = attach_file

        msg = self.create(to, sub, body, mime, attach_file)
        print('create ok')
        self.send(host, port, to, msg)

    def create(self, to, sub, body, mime=None, attach_file=None):
        msg = MIMEMultipart()
        body = MIMEText(body)
        msg['Subject'] = sub
        msg['From'] = self.username
        msg['To'] = to
        msg.attach(body)

        if mime != None and attach_file != None:
            attachment = MIMEBase(mime['type'], mime['subtype'])
            file = open(attach_file['path'], 'rb')
            attachment.set_payload(file.read())
            file.close()
            encoders.encode_base64(attachment)
            msg.attach(attachment)
            attachment.add_header("Content-Disposition", "attachment", filename=attach_file['name'])
        print('create ok')
        return msg

    def send(self, host, port, to, msg):
        smtp = smtplib.SMTP_SSL(host, port)
        print('smtp ok')
        smtp.ehlo()
        print('ehlo ok')
        smtp.login(self.username, self.password)
        print('login ok')
        smtp.mail(self.username)
        smtp.rcpt(to)
        smtp.data(msg.as_string())
        smtp.quit()


class bodyDetect:
    cascade_path = "/usr/local/Cellar/opencv/2.4.13/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
    Cascade = cv2.CascadeClassifier(cascade_path)
    color = (255, 0, 0)

    def __init__(self, img_src):
        self.src = cv2.imread(img_src, 1)
        self.result = self.src
        print('init')
        # self.detect()

    def rectangle(self):
        img_gray = cv2.cvtColor(self.src, cv2.COLOR_BGR2GRAY)
        print('image gray')
        cv2.imwrite('./gray.jpg', img_gray)
        faces = self.Cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))
        ans = faces
        print('yarimasunele')
        if len(faces) > 0:
            print('found')
            for face in faces:
                coordinates = tuple(face[0:2])
                length = tuple(face[0:2] + face[2:4])
                cv2.rectangle(self.result, coordinates, length, self.color, thickness=3)

        cv2.imwrite('./result.jpg', self.result)

        return len(ans)


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        f = request.files['upload']
        f.save("./" + f.filename)

        pic = bodyDetect('./image.jpg')
        print('save')
        if pic.rectangle() > 0:
            to = 'fji810official@gmail.com'
            sub = 'Python'
            body = '114514'
            mime = {'type': 'image', 'subtype': 'jpeg'}
            attach_file = {'name': 'result.jpg', 'path': './result.jpg'}
            sendGmail(to, sub, body, mime, attach_file)
            print('send email')
            print('To {0}   Sub {1} Body {2}'.format(to, sub, body))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
