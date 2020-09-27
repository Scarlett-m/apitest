# coding:utf-8

# !/usr/bin/env python
from flask import Flask, request, session, make_response, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask import render_template, redirect
from app2.stu_api_code.stu_api_opter import ApiOp
import copy
import os
from . import appViews
import datetime
import codecs
# obj_ps = ProjectStatistics()
#
# mysql_host = CONF.mysql_host
# mysql_port = CONF.mysql_port
# mysql_db = CONF.mysql_db



# 创建app的时候已经注册了初始路由 project 故此处只需要写project之后的
@appViews.route("/")
def index():
    # 获取所有的测试用例
    obj_stu_api_op = ApiOp()
    data = obj_stu_api_op.get_ekcollege_test_case()
    return jsonify(**data)

