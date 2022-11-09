import os
import re

from werkzeug.utils import secure_filename

from py.utils.my_exception_util import MyException
from py.result import R
from py.mapper.user_mapper import userMapper
from flask import render_template, Blueprint, request, redirect

bp = Blueprint('login_controller', __name__, url_prefix='/')

#@bp.route('/')
#def index():
 #   return render_template("Login.html")
from flask import Flask, render_template, request, redirect, url_for, session

# -*- coding: utf-8 -*-

info = {}
formc = {}
login_status = [False]

@bp.route('/', methods=['GET', 'POST'])
def login():
    info['message_l'] = '填写并登录'
    info['m_name'] = 'logn'
    if request.method == 'POST':
        #前端得到的输入
        user_name = request.form.get('inputName')
        user_pwd = request.form.get('inputPsw')
        #如果查到使用者，则查询是否密码正确
        if(userMapper.select_by_sql(f"select username from user where username = '{request.form.get('inputName')}'")):
            if(userMapper.select_by_sql(f"select password from user where username='{request.form.get('inputName')}' and password = '{request.form.get('inputPsw')}'")):
        #if (user_name == '1' and user_pwd == '1'):
               return render_template('index.html', info=info)
    else:
            info['message_l'] = '登录失败!'
            info['m_name'] = 'logn'
            login_status[0] = False

    return render_template('login_new.html', info=info)


@bp.route('/Reg/', methods=['GET', 'POST'])
def reg():
    info['message_r'] = '填写并注册'
    if request.method == 'POST':

        formc['name'] = request.form.get('inputName')
        formc['psw'] = request.form.get('inputPsw2')
        formc['email'] = request.form.get('inputEmail')
        formc['tel'] = request.form.get('inputTel')

        userMapper.insert((formc['name'], formc['psw'], formc['email'], formc['tel'],1,1))

        info['message_r'] = '注册成功！'

    else:
            info['message_r'] = '注册失败！'
    return render_template('Reg.html', info=info)







