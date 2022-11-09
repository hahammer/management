# -*- coding:utf-8 -*-
"""
@File : student_entity.py
@Author : 小尹
@Time : 2022/9/30 13:40
"""
class Student:

    def __init__(self, sno, sname, ssex, sage, sclass, sdept):
        self.__sno = str(sno)   # 学号
        self.__sname = sname # 姓名
        self.__ssex = ssex # 性别
        self.__sage = int(sage) # 年龄
        self.__sclass = sclass # 班级
        self.__sdept = sdept # 专业

    def __str__(self):
        return ' '.join((self.__sno, self.__sname, self.__ssex,self.__sage,self.__sclass,self.__sdept))

    def get_sno(self):
        return self.__sno

    def get_sname(self):
        return self.__sname
    def set_sname(self, name):
        self.__sname = name

    def get_ssex(self):
        return self.__ssex
    def set_sex(self, sex):
        self.__ssex = sex

    def get_sage(self):
        return self.__sage
    def set_sage(self, age):
        self.__sage = int(age)

    def get_sclass(self):
        return self.__sclass
    def set_cslass(self, sclass):
        self.__sclass = sclass

    def get_sdept(self):
        return self.__sdept
    def set_csdept(self, sdept):
        self.__sdept = sdept