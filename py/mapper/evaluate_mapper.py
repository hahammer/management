# -*- coding:utf-8 -*-
"""
@File : student_mapper.py
@Author : 小尹
@Time : 2022/9/30 11:53
"""
from py.utils.mysql_util import ConnectMysql, MySql

table_name = "tb_evluation"


# 操作tb_student表，返回一个studentMapper对象用来操作tb_student表
evaluateMapper = MySql(operate_tablename=table_name)
