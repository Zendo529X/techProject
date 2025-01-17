# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting
import os

from flask import Flask
from flask_restx import Api
from Service.TreeService import *
from model.database import db

service = TreeService()

G_api = None
app = Flask(__name__)


# 初始化API routing參數
def initRouting(app):
    G_api = Api(app, version='1.0', title=u'TECHAPI',
                description=u'TECHAPI'
                )
    exposeAPIs(G_api)


# 擴充API路由
def exposeAPIs(pApi):
    from Controller.UserController import api as user
    from Controller.TreeController import api as tree
    from Controller.UploadFileController import api as upload
    pApi.add_namespace(user)
    pApi.add_namespace(tree)
    pApi.add_namespace(upload)


# for test api routing
@app.route('/hello')
def hello_world():
    return 'Hello World123!'


# for test api routing
@app.route('/tree')
def getXmasTree():
    # return service.getHelloXmas()
    return service.getXmasTree()


# mysql sample 的參數
MYSQL = {
    'user': os.getenv('DB_USERNAME', 'dbAdmin'),
    'pw': os.getenv('DB_PWD', 'P$ssw0rd'),
    'db': os.getenv('DB_NAME', 'sample'),
    'host': os.getenv('DB_HOST', 'techdb.mysql.database.azure.com'),
    'port': os.getenv('DB_PORT', '3306'),
}

# mysql CM 的參數
# MYSQL = {
#     'user': os.getenv('DB_USERNAME', 'dbAdmin'),
#     'pw': os.getenv('DB_PWD', 'P$ssw0rd'),
#     'db': os.getenv('DB_NAME', 'CM'),
#     'host': os.getenv('DB_HOST', 'techdb.mysql.database.azure.com'),
#     'port': os.getenv('DB_PORT', '3306'),
# }

# 設定mysql連結
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % MYSQL



# 回收连接
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800
# 每次执行sql前 悲观检查db是否可用;虽然资源稍微额外的消耗,但是简单可靠
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {'pool_pre_ping': True}

# db啟動
db.init_app(app)
# 初始化 API路由
initRouting(app)


# def createDbTable():
#     with app.app_context():
#         db.drop_all()
#         db.create_all()


if __name__ == '__main__':
    # createDbTable()
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
