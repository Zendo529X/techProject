# -*- coding: utf-8 -*-
# @Time : 2023/12/21 下午 03:14
# @Author : Zendo Chiu (segao)
# @Site :
# @File : UserController.py
# @Software: Pycharm
from flask_restx import Namespace, Resource, fields

api = Namespace('user', description='user Data')

@api.route('',methods=["GET", "POST", "DELETE", "PUT"])
class UserController(Resource):

    @api.route("/")
    class createUser(Resource):
        def post(self):
            return