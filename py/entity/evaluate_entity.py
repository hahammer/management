# -*- coding:utf-8 -*-
"""
@File : student_entity.py
@Author : 小尹
@Time : 2022/9/30 13:40
"""
class Evaluate:
    def __init__(self, eno, username, epart1, epart2, epart3, epart4, epart5, epart6, epart7, epart8, epart9, epart10,
                 epart11, epart12, epart13):
        self.__eno = str(eno)
        self.__username = username
        self.__epart1 = epart1
        self.__epart2 = epart2
        self.__epart3 = epart3
        self.__epart4 = epart4
        self.__epart5 = epart5
        self.__epart6 = epart6
        self.__epart7 = epart7
        self.__epart8 = epart8
        self.__epart9 = epart9
        self.__epart10 = epart10
        self.__epart11 = epart11
        self.__epart12 = epart12
        self.__epart13 = epart13


    def __str__(self):
        return ' '.join((self.__eno, self.__username, self.__epart1,
                         self.__epart2, self.__epart3, self.__epart4,
                         self.__epart5, self.__epart6, self.__epart7,
                         self.__epart8, self.__epart9, self.__epart10,
                         self.__epart11, self.__epart12, self.__epart13))

    def get_eno(self):
        return self.__eno

    def get_username(self):
        return self.__username
    def set_username(self, name):
        self.__username = name

    def get_epart1(self):
        return self.__epart1
    def set_epart1(self, number):
        self.__epart1 = number

    def get_epart2(self):
        return self.__epart2
    def set_epart2(self, number):
        self.__epart2 = number

    def get_epart3(self):
        return self.__epart3
    def set_epart3(self, number):
        self.__epart3 = number

    def get_epart4(self):
        return self.__epart4
    def set_epart4(self, number):
        self.__epart4 = number

    def get_epart5(self):
        return self.__epart5
    def set_epart5(self, number):
        self.__epart5 = number

    def get_epart6(self):
        return self.__epart6
    def set_epart6(self, number):
        self.__epart6 = number

    def get_epart7(self):
        return self.__epart7
    def set_epart7(self, number):
        self.__epart7 = number

    def get_epart8(self):
        return self.__epart8
    def set_epart8(self, number):
        self.__epart8 = number

    def get_epart9(self):
        return self.__epart9
    def set_epart9(self, number):
        self.__epart9 = number

    def get_epart10(self):
        return self.__epart10
    def set_epart10(self, number):
        self.__epart10 = number

    def get_epart11(self):
        return self.__epart11
    def set_epart11(self, number):
        self.__epart11 = number

    def get_epart12(self):
        return self.__epart12
    def set_epart12(self, number):
        self.__epart12 = number

    def get_epart13(self):
        return self.__epart13
    def set_epart13(self, number):
        self.__epart13 = number