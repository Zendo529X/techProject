# -*- coding: utf-8 -*-
# @Time : 2023/12/21 下午 03:14
# @Author : Zendo Chiu (segao)
# @Site :
# @File : UserController.py
# @Software: Pycharm
from flask_restx import Namespace, Resource, fields
from Service.UserService import UserService
from model.Users import Users

api = Namespace('user', description='user Data')



@api.route('', methods=["GET", "POST", "DELETE", "PUT"])
class UserController(Resource):
    @api.route("/")
    class createUser(Resource):
        def post(self):
            return

    @api.route("/")
    class getUser(Resource):
        def get(self):
            return UserService.getUser(self)


            # return 'hello get user'
