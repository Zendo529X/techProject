# -*- coding: utf-8 -*-
# @Time : 2023/12/21 下午 01:40
# @Author : Zendo Chiu (segao)
# @Site :
# @File : TreeService.py
# @Software: Pycharm

import json
from printTri import *

from flask import jsonify


class TreeService:

    def getHelloXmas(self):
        return jsonify(message='Hello, API')

    def getXmasTree(self):
        n=4
        m=4
        data = pri(n,m)
        data += priTrunk(n)
        return jsonify(data)

