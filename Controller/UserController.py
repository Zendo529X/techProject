# -*- coding: utf-8 -*-
# @Time : 2023/12/21 下午 03:14
# @Author : Zendo Chiu (segao)
# @Site :
# @File : UserController.py
# @Software: Pycharm
import logging

from flask import request
from flask_restx import Namespace, Resource, fields
from Service.UserService import *
from model.Users import Users
from utils import ApiResponse

api = Namespace('user', description='user Data')
logger = logging.getLogger(__name__)

user_model = api.model('user_model', {
    'id': fields.Integer(required=False, description="id", help="id can be blank."),
    'name': fields.String(required=True, description="name", help="name cannot be blank."),
    'email': fields.String(required=True, description="email", help="email cannot be blank."),
    'cell_phone': fields.String(required=True, description="cell_phone", help="cell_phone cannot be blank.")
})

userService = UserService()

@api.route('', methods=["GET", "POST", "DELETE", "PUT"])
class UserController(Resource):

    def get(self):
        return userService.getUser()

        # return ApiResponse.emitSuccessOutput(data =userService.getUser())

        # return 'hello get user'


    @api.expect(user_model)
    def post(self):
        data = request.get_json()
        return userService.createUser(data)

    @api.expect(user_model)
    def put(self):
        data = request.get_json()
        return userService.updateUser(data)

    @api.expect(user_model)
    def delete(self):
        data = request.get_json()
        return userService.delUser(data)
