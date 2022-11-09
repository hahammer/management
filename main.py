# -*- coding:utf-8 -*-
"""
"""
from flask import Flask
from py.controller.index_controller import bp as bp_index_controller #首页控制层
from py.controller.student_controller import bp as bp_student_controller #学生信息管理控制层
from py.controller.model_controller import bp as bp_model_controller #模型信息管理控制层
from py.controller.login_controller import bp as bp_login_controller #登录信息管理控制层
from py.controller.user_controller import bp as bp_user_controller
from py.controller.evaluate_controller import bp as bp_evaluate_controller
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False # 防止后端返回给前端的数据中文内容乱码

app.register_blueprint(bp_login_controller)
app.register_blueprint(bp_index_controller)
app.register_blueprint(bp_student_controller)
app.register_blueprint(bp_model_controller)
app.register_blueprint(bp_user_controller)
app.register_blueprint(bp_evaluate_controller)



if __name__ == '__main__':
    # app.run(host='127.0.0.1',port=80)
    app.run()