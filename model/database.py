# -*- coding: utf-8 -*-
# @Time : 2023/12/26 下午 02:19
# @Author : Zendo Chiu (segao)
# @Site :
# @File : Users.py
# @Software: Pycharm

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"autoflush": False})
