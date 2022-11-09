# -*- coding:utf-8 -*-
"""
@File : mysql_util.py
@Author : 小尹
@Time : 2022/9/30 11:14
"""
'''
自定义封装mysql
'''
import pymysql

# 从配置文件中读取连接mysql的信息
def connect_mysql():
    mysql_config = {}
    try:
        with open("C:\\Users\hahammer\Desktop\ManagementSystem\config\mysql_config.txt", mode="r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("#"):
                    continue
                r = line.strip().split("=")
                mysql_config[r[0]] = r[1]
                if r[0].lower() == "port":
                    mysql_config[r[0].lower()] = int(r[1])
        return mysql_config
    except Exception as e:
        raise Exception(f"配置有文件异常！！！\n{e}")

# 必须先连接数据库
class ConnectMysql:
    CONNECT_MYSQL_DB_OBJ = None
    @staticmethod
    def connect_mysql(my_sqldb_config_param: dict):
        print("connect_mysql...")
        assert isinstance(my_sqldb_config_param, dict), "请以字典类型的格式传入！"
        try:
            ConnectMysql.CONNECT_MYSQL_DB_OBJ = pymysql.connect(**my_sqldb_config_param)  # 连接数据库，配置参数
            print(f"{my_sqldb_config_param['database']}————数据库连接成功")
        except Exception as e:
            raise Exception(f"数据库连接失败！！！\n请检查数据库配置参数是否正确或检查本地数据库是否已启动！\n{e}")
    @staticmethod
    def create_table(sql):
        try:
            cursor = ConnectMysql.CONNECT_MYSQL_DB_OBJ.cursor()
            cursor.execute(sql)  # 执行sql语句
            ConnectMysql.CONNECT_MYSQL_DB_OBJ.commit() # 执行sql语句后，进行提交
            cursor.close()
            print("表创建成功")
        except Exception as e:
            ConnectMysql.CONNECT_MYSQL_DB_OBJ.rollback()  # 执行sql语句失败，进行回滚
            print("表创建失败：",e)

ConnectMysql.connect_mysql(connect_mysql())

# 操作某一个表类
class MySql:
    def __init__(self, operate_tablename:str):
        self._operate_tablename = operate_tablename
        try:
            self._conn = ConnectMysql.CONNECT_MYSQL_DB_OBJ
            self._cursor = self._conn.cursor() # 创建一个游标，用来执行查询
            self._get_field() # 获取此表中的字段名
        except Exception as e:
            raise Exception(f"数据库连接失败！！！\n请检查表名、配置参数是否正确或检查本地数据库是否已启动！\n{e}")

    # 获取_conn对象
    @property
    def get_connect(self):
        return self._conn
    # 获取_cursor对象
    @property
    def get_cursor(self):
        return self._cursor
    # 获取__desc对象
    @property
    def get_description(self):
        # print(f"{self._operate_tablename}表中的字段属性：",self._desc)
        return self._desc
    # 获取正在操作的表名
    @property
    def operate_tablename(self):
        return f"正在操作 {self._operate_tablename}表！！！"
    # 修改要操作的表
    @operate_tablename.setter
    def operate_tablename(self,operate_tablename):
        assert operate_tablename !="", "请输入要操作的表名！"
        print(f"{self._operate_tablename} 表已被更换！")
        self._operate_tablename = operate_tablename
        self._get_field()
    # 获取此表中的字段名
    def _get_field(self):
        self._cursor.execute(f"select * from {self._operate_tablename}")
        self._desc = self._cursor.description
        self._field_ = []
        for field in self._desc:
            self._field_.append(field[0])
    # 执行sql语句
    def _sql(self,sql,msg=""):
        try:
            self._cursor.execute(sql)  # 执行sql语句
            self._conn.commit() # 执行sql语句后，进行提交
            if msg:print(f"数据{msg}成功！")
            return True
        except Exception as e:
            if msg:print(f"\033[31m数据{msg}失败！！！\n{e} \033[0m")
            self._conn.rollback()  # 执行sql语句失败，进行回滚
            return False
    # 插入数据
    def insert(self, *value):
        if not isinstance(value[0],tuple): raise Exception("要求传入的参数类型为tuple元组！！！")
        if len(value) == 1: value=value[0]
        else:value = str(value)[1:-1]
        sql = f"insert into {self._operate_tablename}({','.join(self._field_[1:])}) values {value}"
        if not self._sql(sql,f"{value}插入"):
            print("\n\033[31m：请检查每一条记录字段是否正确！！！\033[0m\n")
    # 插入：自定义sql语句插入数据
    def insert_by_sql(self, sql):
        self._sql(sql,"插入")
    # 删除：通过id删除该条数据
    def delete_by_id(self,id_:int):
        sql = f"delete from {self._operate_tablename} where id = {id_}"
        if self._sql(sql):print(f"id={id_}记录，删除成功！")
        else:print(f"\n\033[31m：id = {id_}记录，删除失败！！！\033[0m\n")
    # 删除：自定义sql语句删除数据
    def delete_by_sql(self, sql):
        self._sql(sql,"删除")
    # 修改：通过id修改数据
    def update_by_id(self, id_:int, set_field:dict):
        assert isinstance(set_field,dict),"请以字典类型的格式传入！"
        tempset_field = []
        for i in set_field:
            tempset_field.append(f"{i}='{set_field[i]}'")
        set_field = ",".join(tempset_field)
        sql = f"update {self._operate_tablename} set {set_field} where id = {id_}"
        if self._sql(sql):print(f"id={id_}记录，{set_field}修改成功！")
        else:print(f"\n\033[31m：id = {id_}记录，{set_field}修改失败！！！\033[0m\n")
    # 修改：自定义sql语句修改数据
    def update_by_sql(self, sql):
        self._sql(sql,"修改")
    # 查询：通过id查询一条数据
    def select_by_id(self,id_:int,field="*"):
        if field != "*": field = ','.join(field)
        sql = f"select {field} from {self._operate_tablename} where id={id_}"
        self._cursor.execute(sql)
        return self._cursor.fetchone()
    # 查询：指定查询多少条数数据,可根据简单条件查询（where 字段=”“）
    def select_many(self,num:int,query_builder=None,field="*"):
        if field != "*": field = ','.join(field)
        sql = f"select {field} from {self._operate_tablename}"
        if query_builder:
            if isinstance(query_builder,dict) and len(query_builder) == 1:
                query_builder = list(query_builder.items())[0]
                sql = f"select {field} from {self._operate_tablename} where {query_builder[0]}='{query_builder[1]}'"
            else: raise Exception("要求输入的条件为dict(字典)类型并且只能有一对键值（：len(dict）=1）！！！")
        self._cursor.execute(sql)
        return self._cursor.fetchmany(num)
    # 查询：所有数据
    def select_all(self, field="*"):
        if field != "*": field = ','.join(field)
        sql = f"select {field} from {self._operate_tablename}"
        self._cursor.execute(sql)
        return self._cursor.fetchall()
    # 查询：自定义sql语句查询数据
    def select_by_sql(self, sql):
        try:
            self._cursor.execute(sql)
            return self._cursor.fetchall()
        except Exception as e:
            print(f"\033[31m：数据查询失败！！！\n{e} \033[0m")

    # 实体类映射，返回的记录带有该表中的字段（以字典的形式）
    def MapEntity(self, db_return_result: tuple):
        assert isinstance(db_return_result, tuple), "请以tuple元组类型的格式传入！"
        try:
            if not isinstance(db_return_result[0],tuple):
                return dict(zip(self._field_, db_return_result))
            return [dict(zip(self._field_, i)) for i in db_return_result]
        except Exception as e:
            print("可将从实例化数据库对象调用的方法直接传入这里！！！")
            raise Exception(f"可将从实例化数据库对象调用的方法直接传入这里！！！\n {e}")

    # 当对象被销毁时，游标关闭
    def __del__(self):
        print(f"{self._operate_tablename} >>> _cursor close...")
        self._cursor.close()