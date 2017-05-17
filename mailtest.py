# -*- coding: utf-8 -*-
#Camera
import picamera
import io
import numpy as np
import cv2


import os.path
import datetime
import smtplib
from email import Encoders
from email.Utils import formatdate
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


stream = io.BytesIO()

cascade_path = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_path)

CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

color = (255,255,255)
camera = picamera.PiCamera()
camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)

ADDRESS = "deraderapyon"
PASSWARD = "dera0721"
SMTP = "smtp.gmail.com"
PORT = 587

def main():
    while True:
        camera.capture(stream,format='jpeg')
        data = np.fromstring(stream.getvalue(),dtype=np.uint8)
        image = cv2.imdecode(data,1)

        image_gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

        if len(facerect)>0:
            print "found"
            send_message()
            break

        stream.seek(0)

    print "send massage"

def create_massage(from_addr, to_addr, subject, body,mime=None,attach_file=None):
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Date"] = formatdate()
    msg["Subject"] = subject
    body = MIMEText(body)
    msg.attach(body)

    if mime != None and attach_file != None:
        attachment = MIMEBase(mime['type'],mime['subtype'])
        file = open(attach_file['path'])
        attachment.set_payload(file.read())
        file.close()
        Encoders.encode_base64(attachment)
        msg.attach(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=attach_file['name'])

    return msg

def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP(SMTP, PORT)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(ADDRESS,PASSWARD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()

def send_message():
    to_addr = "yohei.onodera.5x@stu.hosei.ac.jp"

    subject = "subject"
    body = "body"

    msg = create_massage(ADDRESS, to_addr, subject, body)
    send(ADDRESS, [to_addr], msg)


if __name__ == '__main__':
    main()