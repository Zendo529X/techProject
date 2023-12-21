# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting

from flask import Flask
from Service.TreeService import *

service = TreeService();

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World1!'


@app.route('/tree')
def getXmasTree():
    return service.getHelloXmas()


if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
