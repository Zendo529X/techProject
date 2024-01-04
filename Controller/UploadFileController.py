# -*- coding: utf-8 -*-
# @Time : 2024/1/3 上午 10:52
# @Author : Zendo Chiu (segao)
# @Site :
# @File : UploadFileController.py
# @Software: Pycharm

from flask import request
from flask_restx import Namespace, Resource, fields
from Service.UserService import *
from Service.UploadFileService import *

api = Namespace('uploadFile', description='user Data')

user_model = api.model('user_model', {
    'id': fields.Integer(required=False, description="id", help="id can be blank."),
    'name': fields.String(required=True, description="name", help="name cannot be blank."),
    'email': fields.String(required=True, description="email", help="email cannot be blank."),
    'cell_phone': fields.String(required=True, description="cell_phone", help="cell_phone cannot be blank.")
})

userService = UserService()
uploadFileService = UploadFileService()


@api.route('', methods=["GET", "POST", "DELETE", "PUT"])
class UploadFileController(Resource):
    @api.route("/uploadACPnL")
    class UploadPayment(Resource):
        def post(self):
            data = request.files['file'].read()
            if data is None or data == '':
                return ApiResponse.emitErrorOutput(E_CREATE_FAIL, "無資料上傳", "no data")

            return uploadFileService.upLoadACP(data)

    @api.route("/uploadAFPnL")
    class UploadPayment(Resource):
        def post(self):
            data = request.files['file'].read()
            if data is None or data == '':
                return ApiResponse.emitErrorOutput(E_CREATE_FAIL, "無資料上傳", "no data")

            return uploadFileService.upLoadAFP(data)
