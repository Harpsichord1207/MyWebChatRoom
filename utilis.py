#!/usr/bin/env python  
# -*- coding:utf-8 -*- 

""" 
@version: v1.0 
@author: Harp
@contact: liutao25@baidu.com 
@software: PyCharm 
@file: utilis.py.py 
@time: 2018/2/26 0026 23:07 
"""

from json import dumps


def json_orm(log, ip):
    dic = {
        # 'id': log.id,
        'username': log['username'],
        # 'address': generate_hash(log.address),
        'content': log['content'],
        'avatar_id': log['avatar_id'],
        'chat_time': str(log['chat_time']),
        'status': 'self' if log['address'] == ip else 'other'
    }
    return dumps(dic, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    pass
