# -*- coding:utf-8 -*-
"""
@File : student_entity.py
@Author : 小尹
@Time : 2022/9/30 13:40
"""
class User:
    def __init__(self, id, eno, username, p, fullname, email, phone, status):
        self.__id = str(eno)   # 学号
        self.__eno = str(eno)   # 学号
        self.__username = username # 姓名
        self.__password = p
        self.__fullname = fullname
        self.__email = email
        self.__phone = phone
        self.__status = status


    def __str__(self):
        return ' '.join((self.__eno, self.__username, self.__fullname, self.__email,
                         self.__phone, self.__status))

    def get_eno(self):
        return self.__eno
    def get_id(self):
        return self.__id
    def get_username(self):
        return self.__username
    def set_username(self, name):
        self.__username = name
    def get_password(self):
        return self.__password
    def set_password(self, p):
        self.__password = p
    def get_fullname(self):
        return self.__fullname
    def set_fullname(self, name):
        self.__fullname = name

    def get_email(self):
        return self.__email
    def set_email(self, number):
        self.__email = number

    def get_phone(self):
        return self.__phone
    def set_epart3(self, number):
        self.__phone = number

    def get_status(self):
        return self.__status
    def set_status(self, number):
        self.__status = number


