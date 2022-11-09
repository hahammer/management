# -*- coding:utf-8 -*-
"""
@File : student_controller.py
@Author : 小尹
@Time : 2022/9/30 11:54
"""
import re
from py.mapper.evaluate_mapper import evaluateMapper
from py.entity.evaluate_entity import Evaluate
from py.utils.my_exception_util import MyException
from py.result import R
from flask import render_template, Blueprint, request

bp = Blueprint('evaluate_controller', __name__, url_prefix='/')

# 默认访问（首页）
@bp.route('/evaluateSystem', methods=['POST','GET'])
def evaluate_system():
    return render_template('evaluate_management.html')

@bp.route('/evaluateSystem/getAllEvaluate')
def get_all_evaluate():
    try:
        return R.success(evaluateMapper.MapEntity(evaluateMapper.select_all()))
    except Exception as e:
        return R.error(message=f"查询失败\n{str(e)}")

# 保存
@bp.route('/evaluateSystem/saveEvaluate/<id>')
def save_evaluation_by_id(id):
    try:
        print(id)
        sql = "select * from tb_evluation where id = {}".format(id)
        print(sql)
        f = evaluateMapper.MapEntity(evaluateMapper.select_by_sql(sql))
        print(f)
        return R.success(message="保存成功")
    except Exception as e:
        print(e)
        return R.error(message=f"保存失败\n{str(e)}")



