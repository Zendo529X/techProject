# -*- coding: utf-8 -*-
# @Time : 2023/12/26 下午 02:29
# @Author : Zendo Chiu (segao)
# @Site :
# @File : Users.py
# @Software: Pycharm

from model.database import db


class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column('id', db.Integer, primary_key=True)
