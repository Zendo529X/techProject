# -*- coding: utf-8 -*-
# @Time : 2023/12/26 下午 02:29
# @Author : Zendo Chiu (segao)
# @Site :
# @File : Users.py
# @Software: Pycharm
from datetime import datetime
from model.database import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(50))
    cell_phone = db.Column(db.String(50))
    create_at = db.Column(db.DateTime, default=datetime.now())
    update_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<USERS %r>' % self.id

    def create(self, data):
        db.session.add(data)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, id):
        od = self.query.get(id)
        if od is not None:
            db.session.delete(od)
            return db.session.commit()
