# -*- coding:utf-8 -*-
"""

"""
from py.utils.mysql_util import ConnectMysql, MySql

table_name = "tb_student"




# 操作tb_student表，返回一个studentMapper对象用来操作tb_student表
studentMapper = MySql(operate_tablename=table_name)
