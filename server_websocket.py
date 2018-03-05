#!/usr/bin/env python  
# -*- coding:utf-8 -*- 

""" 
@version: v1.0 
@author: Harp
@contact: liutao25@baidu.com 
@software: PyCharm 
@file: server_websocket.py 
@time: 2018/2/27 0027 15:52 
"""

from flask import Flask, render_template, request, session
from flask_socketio import SocketIO
import config
from models import return_last_log, insert_log
from utilis import json_orm
from datetime import datetime


app = Flask(__name__)
app.config.from_object(config)
socketio = SocketIO(app)


@app.route('/')
def page():
    session['ip'] = request.remote_addr
    return render_template('ChatRoom.html')


@app.route('/api/get/')
def api_get():
    return json_orm(return_last_log(), request.remote_addr)


@socketio.on('message')
def handler_message(data):
    # print('here', data, loads(data),type(data))
    chat_time = str(datetime.now())[:19]
    log = {
        'username': data.get('user'),
        'content': data.get('msg'),
        'chat_time': chat_time,
        'address': session['ip'],
        'avatar_id': data.get('avatar_id')
    }
    insert_log(log)
    socketio.emit('res')


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=80)
