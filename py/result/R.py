# -*- coding:utf-8 -*-
"""
@File : R.py
@Author : 小尹
@Time : 2022/9/30 11:55
"""
"""
统一后端返回给前端的数据格式
code #返回状态码
message #返回消息
data #返回数据
"""

def success(data:list=None,message="成功"):
    return {
        "code":200,
        "data": data,
        "message": message,
        }

def error(data:list=None,message="失败"):
    return {
        "code": 201,
        "data": data,
        "message": message,
    }