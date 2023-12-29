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

    def createUser(self):
        return

    def updateUser(self):
        return

    def delUser(self):
        return