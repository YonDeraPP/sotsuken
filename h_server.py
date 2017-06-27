#-*-coding:utf-8-*-

from flask import Flask
from flask import request
import json
import ast

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    if request.method == 'POST':
        f = request.data
        
        
    return flask.jsonify(res='ok')

if __name__ == '__main__':
    app.run()
