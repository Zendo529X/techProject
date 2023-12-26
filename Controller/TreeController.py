# -*- coding: utf-8 -*-
# @Time : 2023/12/21 下午 03:14
# @Author : Zendo Chiu (segao)
# @Site :
# @File : UserController.py
# @Software: Pycharm

from flask_restx import Namespace, Resource, fields

api = Namespace('tree', description='tree Data')

request_treeLevel_treeWeight = api.model('request_treeLevel_treeWeight', {
    'level': fields.String(required=True, description="level", help="level cannot be blank."),
    'weight': fields.String(required=True, description="weight", help="site cannot be blank.")
    })

@api.route('',methods=["GET", "POST", "DELETE", "PUT"])
class TreeController(Resource):

    @api.route("/")
    class createTree(Resource):
        def post(self):
            return

    @api.route("/")
    class getTree(Resource):
        def get(self):
            return

    @api.route("xmas")
    class getXmasTree(Resource):
        @api.expect(request_treeLevel_treeWeight)
        def post(self):
            return
