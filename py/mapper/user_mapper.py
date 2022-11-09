# -*- coding:utf-8 -*-

from py.utils.mysql_util import ConnectMysql, MySql

table_name = "user"


# 操作"usert表，返回一个"userMapper对象用来操作"user表
userMapper = MySql(operate_tablename=table_name)
