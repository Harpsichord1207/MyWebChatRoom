#!/usr/bin/env python  
# -*- coding:utf-8 -*- 

""" 
@version: v1.0 
@author: Harp
@contact: liutao25@baidu.com 
@software: PyCharm 
@file: models.py 
@time: 2018/2/26 0026 21:28 
"""

from pymongo import MongoClient, DESCENDING

client = MongoClient('localhost', 27017)
db = client.chatdb
col = db.chat_log


def return_last_log():
    return col.find_one(sort=[('chat_time', DESCENDING)])


def insert_log(log):
    col.insert(log)

