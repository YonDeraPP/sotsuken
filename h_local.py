# -*-coding:utf-8-*-

import requests
import json
import io
import base64

def Capture():
    data = open("image.jpg","rb")
    return data


url = 'http://localhost:5000'
data = Capture()
files = {'upload':data}

res = requests.post(url, files = files)

print(res)
