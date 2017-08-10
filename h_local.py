# -*-coding:utf-8-*-

import requests
import json
import io
import base64
import datetime

def Capture():
    data = open("image.jpg" , "rb")
    return data


url = 'http://localhost:8000'
data_ = Capture()

files = {'upload':data_ }

#print(type(datetime.date.today().strftime("%YY-%m-%d %H:%M:%S")))
res = requests.post(url, files = files)
print(res)

res = requests.get(url+"/empty")
print(res)
