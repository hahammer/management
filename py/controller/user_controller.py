# -*- coding:utf-8 -*-
"""
@File : student_controller.py
@Author : 小尹
@Time : 2022/9/30 11:54
"""
import re
from py.mapper.user_mapper import userMapper
from py.entity.user_entity import User
from py.utils.my_exception_util import MyException
from py.result import R
from flask import render_template, Blueprint, request

bp = Blueprint('user_controller', __name__, url_prefix='/')

# 默认访问（首页）
@bp.route('/userSystem')
def user_system():
    return render_template('user_management.html')

# 添加用户
@bp.route('/userSystem/addUser',methods=["POST"])
def add_student():
    form_data = request.get_json()
    try:
        if len(form_data) != 6:
            raise MyException("数据不能为空！")
        if not re.match("^[0-9]{1,20}$", form_data['sno']):
            raise MyException("学号长度最长为20且为数字字符！")
        if userMapper.select_by_sql(f"select sno from tb_student where sno = '{form_data['sno']}'"):
            raise MyException("该学号已被使用！")
        if not form_data['sname'].isalpha():
            raise MyException("姓名只能包含中英文，不能包含数字和其他字符。")
        if not form_data['ssex'] in ('男', '女'):
            raise MyException("性别只能是男或女")
        try:
            int(form_data['sage'])
        except:
            raise MyException("年龄只能是正整数")
        s = User(**form_data)
        userMapper.insert((s.get_sno(),s.get_sname(),s.get_ssex(),s.get_sage(),s.get_sclass(),s.get_sdept()))
        return R.success(message="添加成功")
    except Exception as e:
        return R.error(message=f"添加失败\n{str(e)}")

@bp.route('/userSystem/getAllUser')
def get_all_user():
    try:
        return R.success(userMapper.MapEntity(userMapper.select_all()))
    except Exception as e:
        return R.error(message=f"查询失败\n{str(e)}")

# 条件查询，根据用户姓名
@bp.route('/userSystem/conditionQuery/<snameQuery>')
def get_one_user_by_sname(snameQuery):
    try:
        sql = f"select * from user where username like '{snameQuery}%'"
        return R.success(userMapper.MapEntity(userMapper.select_by_sql(sql)))
    except Exception as e:
        return R.error(message=f"查询失败\n{str(e)}")

@bp.route('/userSystem/updateUser/<id>')
def update_user_by_id(id):
    try:
        return R.success(userMapper.MapEntity(userMapper.select_by_id(id)))
    except Exception as e:
        return R.error(message=f"编辑失败\n{str(e)}")
# 修改学生通过id
@bp.route('userSystem/updateUser',methods=["POST"])
def update_user_by_id2():
    try:
        form_data = request.get_json()
        if not form_data['username'].isalpha():
            raise MyException("姓名只能包含中英文，不能包含数字和其他字符。")
        if not form_data['ssex'] in ('男', '女'):
            raise MyException("性别只能是男或女")
        try:
            int(form_data['sage'])
        except:
            raise MyException("年龄只能是正整数")
        userMapper.update_by_id(form_data.pop('id'), form_data)
        return R.success(message="修改成功")
    except Exception as e:
        print(e)
        return R.error(message=f"修改失败\n{str(e)}")

# 删除
@bp.route('/userSystem/deleteUser/<id>')
def delete_user_by_id(id):
    try:
        userMapper.delete_by_id(id)
        return R.success(message="删除成功")
    except Exception as e:
        print(e)
        return R.error(message=f"删除失败\n{str(e)}")


@bp.route('userSystem/checkUser',methods=["POST"])
def check_user():
    try:
        form_data = request.get_json()
        sql = f"select * from tb_evluation where username like '{form_data['username']}%'"
        return R.success(userMapper.MapEntity(userMapper.select_by_sql(sql)))

    except Exception as e:
        print(e)
        return R.error(message=f"修改失败\n{str(e)}")

