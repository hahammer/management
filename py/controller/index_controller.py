# -*- coding:utf-8 -*-

from flask import render_template, Blueprint, redirect

bp = Blueprint('index_controller', __name__, url_prefix='/')

# 默认访问
@bp.route('/')
def index():
    return render_template("index.html")

# 首页默认加载初始页面
@bp.route('/index_v1_0')
def index_v1_0():
    return render_template("index-v1-0.html")

# 班上学生男女比例可视化
from pyecharts import options as opts
from pyecharts.charts import Pie
from py.mapper.student_mapper import studentMapper
@bp.route('/index_v1_0/sex')
def pie_rosetype():
    sex = studentMapper.select_by_sql("select ssex from tb_student")
    c = (
        Pie()
            .add(
            "",
            [["男生",sex.count(('男',))],["女生",sex.count(('女',))]],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
    )
    return c.dump_options_with_quotes()