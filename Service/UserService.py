# -*- coding: utf-8 -*-
# @Time : 2023/12/21 下午 04:50
# @Author : Zendo Chiu (segao)
# @Site :
# @File : UserService.py
# @Software: Pycharm
import logging

from model.Users import Users
from model.ACPnL import ACPnL
from model.AFPnL import AFPnL
from utils.ApiResponse import *
from datetime import datetime
import json
from view.users import UsersSchema

# todo add user service

logger = logging.getLogger(__name__)


class UserService:
    def getUser(self):
        users = Users.query.all()

        schema = UsersSchema()
        result = schema.dumps(users, many=True)
        result = json.loads(result)
        return ApiResponse.emitSuccessOutput(data=result)

    def getUserById(self, id):
        user = Users.query.filter(Users.id == id).first()
        return user

    def getUserByPhone(self, cell_phone):
        user = Users.query.filter(Users.cell_phone == cell_phone).first()
        return user

    def createUser(self, data):
        logger.info("create user start")
        id = data.get('id', None)
        cell_phone = data.get('cell_phone', None)
        name = data.get('name', None)
        email = data.get('email', None)
        if id is not None or cell_phone is not None:
            user = None
            if id is not None:
                user = self.getUserById(id)
            elif cell_phone is not None:
                user = self.getUserByPhone(cell_phone)

            if user is not None:
                logger.debug("create user failed")
                return ApiResponse.emitErrorOutput(E_QUERY_FAIL, "data existed", "user existed")
            else:

                user = Users()
                user.id = id
                user.name = name
                user.email = email
                user.cell_phone = cell_phone
                user.created_at = datetime.now()
                user.updated_at = datetime.now()
                user.create(user)
                logger.debug("create user successes")
                return ApiResponse.emitSuccessOutput("create user successes")

    def updateUser(self, data):
        id = data.get('id', None)
        cell_phone = data.get('cell_phone', None)
        name = data.get('name', None)
        email = data.get('email', None)
        if id is not None or cell_phone is not None:
            user = None
            if id is not None:
                user = self.getUserById(id)
            elif cell_phone is not None:
                user = self.getUserByPhone(cell_phone)

            if user is None:
                return ApiResponse.emitErrorOutput(E_QUERY_FAIL, "data not existed", "user not existed")
            else:

                user = self.getUserById(id)
                user.name = name
                user.email = email
                user.cell_phone = cell_phone
                user.updated_at = datetime.now()
                Users.update(user)
                return ApiResponse.emitSuccessOutput("create user successes")

    def delUser(self, data):
        id = data.get('id', None)
        cell_phone = data.get('cell_phone', None)
        name = data.get('name', None)
        email = data.get('email', None)
        user = None
        if id is not None:
            user = self.getUserById(id)
        if user:
            user.user_del_status = True
            user.updated_at = datetime.now()
            Users.update(user)
            return ApiResponse.emitSuccessOutput("delete user successes")
        else:
            return ApiResponse.emitErrorOutput(E_QUERY_FAIL, "data not existed", "user not existed")
