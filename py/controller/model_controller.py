
import re
import time
import shutil,os
from py.mapper.model_mapper import modelMapper
from py.entity.model_entity import Model
from py.utils.my_exception_util import MyException
from py.result import R
from flask import render_template, Blueprint, request

bp = Blueprint('model_controller', __name__, url_prefix='/')

# 默认访问（首页）
@bp.route('/modelSystem')
def modle_system():
    return render_template('modle_management.html')

# 查询所有模型
@bp.route('/modelSystem/getAllModel')
def get_all_model():
    try:
        return R.success(modelMapper.MapEntity(modelMapper.select_all()))
    except Exception as e:
        return R.error(message=f"查询失败\n{str(e)}")

print(modelMapper.MapEntity(modelMapper.select_all()))


# 添加模型
@bp.route('/modelSystem/addModel',methods=["POST"])
def add_model():
  form_data = request.get_json()
  try:
    m = Model(**form_data)
    print(form_data)
    modelMapper.insert((m.get_model_name(), m.get_model_no(), m.get_model_factory(), m.get_model_size(), m.get_model_texture(), m.get_model_document()))
    return R.success(message="添加成功")
  except Exception as e:
    return R.error(message=f"添加失败\n{str(e)}")



 #根据文件的路径，把文件转移到指定目录下
    #m.get_model_document()是文件的路径，现在把该文件的路径的文件名称m.get_model_name()，转移到指定的路径之下
  model_name = m.get_model_name()
  model_path = m.get_model_document()

  # 复制单个文件
  path1 = m.get_model_document()

  path2 = 'C:\\Users\hahammer\Desktop'
  #把path1的文件转到path2中
  shutil.move(path1, path2)

  print(m.get_model_document())





#修改模型
@bp.route('/modelSystem/updateModel/<id>')
def update_model_by_id(id):
    try:
        return R.success(modelMapper.MapEntity(modelMapper.select_by_id(id)))
    except Exception as e:
        return R.error(message=f"编辑失败\n{str(e)}")

# 修改模型通过id
@bp.route('/modelSystem/updateModel',methods=["POST"])
def update_student_by_id2():
    try:
        form_data = request.get_json()

        modelMapper.update_by_id(form_data.pop('id'), form_data)
        return R.success(message="修改成功")
    except Exception as e:
        print(e)
        return R.error(message=f"修改失败\n{str(e)}")

# 删除模型通过id
@bp.route('/modelSystem/deleteModel/<model_name>')
def delete_student_by_id(model_name):
    try:
        modelMapper.delete_by_id(model_name)
        return R.success(message="删除成功")
    except Exception as e:
        print(e)
        return R.error(message=f"删除失败\n{str(e)}")

# 条件查询，根据模型名称
@bp.route('/modelSystem/conditionQuery/<snameQuery>')
def get_one_student_by_sname(snameQuery):
    try:
        sql = f"select * from tb_model where model_name like '{snameQuery}%'"
        return R.success(modelMapper.MapEntity(modelMapper.select_by_sql(sql)))
    except Exception as e:
        return R.error(message=f"查询失败\n{str(e)}")
