# -*- coding:utf-8 -*-
"""
@File : my_exception_util.py
@Author : 小尹
@Time : 2022/9/30 15:47
"""
# 自定义异常类
class MyException(Exception):
    def __init__(self,error_msg):
        Exception.__init__(self)
        self.__error_msg = error_msg
    def __str__(self):
        return "异常："+self.__error_msg