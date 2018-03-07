#!/usr/bin/env python  
# -*- coding:utf-8 -*- 

""" 
@version: v1.0 
@author: Harp
@contact: liutao25@baidu.com 
@software: PyCharm 
@file: admin_views.py.py 
@time: 2018/3/7 0007 21:55 
"""

from flask import Blueprint, render_template, request
from models import return_last_n_logs

admin = Blueprint('admin', __name__)


@admin.route('/')
def log_history():
    n = int(request.args.get('n', '10'))
    auth = request.args.get('auth', 'wrong')
    if auth != 'lll':
        return '<h3>404 not found</h3>', 404
    logs = return_last_n_logs(n)
    return render_template('history.html', logs=logs)


if __name__ == "__main__":
    pass
