#-*-coding:utf-8-*-

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

cascade_path = "/usr/local/Cellar/opencv/2.4.13/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
Cascade = cv2.CascadeClassifier(cascade_path)

class sendGmail:
    username, password = '14514', '****'

    def __init__(self, to, sub, body, mime, attach_file):
        host, port = 'smtp.gmail.com', 465
        msg = MIMEMultipart()
        body = MIMEText(body)
        msg['Subject'] = sub
        msg['From'] = self.username
        msg['To'] = to
        msg.attach(body)

        attachment = MIMEBase(mime['type'], mime['subtype'])
        file = open(attach_file['path'],'rb')
        attachment.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment)
        msg.attach(attachment)
        attachment.add_header("Content-Disposition","attachment", filename=attach_file['name'])

        smtp = smtplib.SMTP_SSL(host,port)
        smtp.ehlo()
        smtp.login(self.username, self.password)
        smtp.mail(self.username)
        smtp.rcpt(to)
        smtp.data(msg.as_string())
        smtp.quit()

@app.route('/',methods=['POST'])
def index():
    if request.method == 'POST':
        f = request.files['upload']
        f.save("./"+f.filename)

        img_src = cv2.imread("./image.jpg",1)
        img_result = img_src
        img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
        faces = Cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(100,100))

        if len(faces) > 0:
            color = (255, 0, 0)
            print('found')
            for face in faces:
                coordinates = tuple(face[0:2])
                length = tuple(face[0:2] + face[2:4])
                cv2.rectangle(img_result, coordinates, length, color, thickness=3)
                cv2.imwrite("./result.jpg",img_result)
                print("save")
                to = 'fji810official@gmail.com'
                sub = 'Python'
                body = '114514'
                mime = {'type':'image', 'subtype':'jpeg'}
                attach_file={'name':'result.jpg', 'path':'./result.jpg'}
                sendGmail(to, sub, body,mime,attach_file)
                print('send email')
                
                
    return flask.jsonify(res='ok')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
