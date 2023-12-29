# -*- coding: utf-8 -*-
# @Time : 2023/12/21 下午 04:50
# @Author : Zendo Chiu (segao)
# @Site :
# @File : UserService.py
# @Software: Pycharm

from model.Users import Users


# todo add user service

class UserService:
    def getUser(self):
        users = Users.query.all()
        return users

    def createUser(self, data):
        id = data.get('id',None)
        name = data.get('name',None)
        email = data.get('email',None)
        cell_phone=data.get('cell_phone',None)
        user = Users()
        user.id = id
        user.name=name
        user.email =email
        user.cell_phone = cell_phone
        user.create(user)
        return

    def updateUser(self):
        return

    def delUser(self):
        return
