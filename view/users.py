# -*- coding: utf-8 -*-
# @Time : 2024/6/13 下午 04:12
# @Author : Zendo Chiu (segao)
# @Site :
# @File : users.py
# @Software: Pycharm

from marshmallow import Schema, fields


class UsersSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Str()
    cell_phone = fields.Str()
    user_del_status = fields.Bool()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    # pCode = fields.Str()
    # description = fields.Str()
    # remark = fields.Str()
