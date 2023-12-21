# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting

from flask import Flask
from flask_restplus import Api
from Service.TreeService import *

service = TreeService();

app = Flask(__name__)

initRouting(app)

def initRouting(app):
    G_api = Api(app, version='1.0', title=u'TECHAPI',
                description=u'TECHAPI'
                )
    exposeAPIs(G_api)

def exposeAPIs(pApi):
    from Controller.UserController import api as user

@app.route('/')
def hello_world():
    return 'Hello World1!'


@app.route('/tree')
def getXmasTree():
    # return service.getHelloXmas()
    return service.getXmasTree()


if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
