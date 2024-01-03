# -*- coding: utf-8 -*-
# @Time : 2024/1/3 上午 09:41
# @Author : Zendo Chiu (segao)
# @Site :
# @File : AFPnL.py
# @Software: Pycharm
from model.database import db


class AFPnL(db.Model):
    __tablename__ = 'AFPnL'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    YYYY = db.Column(db.String(10))
    MM = db.Column(db.String(10))
    org0 = db.Column(db.String(50))
    org1 = db.Column(db.String(50))
    org2 = db.Column(db.String(50))
    orgName = db.Column(db.String(50))
    Revenue = db.Column(db.Numeric)
    COGS = db.Column(db.Numeric)
    GP = db.Column(db.Numeric)
    ImpExp = db.Column(db.Numeric)
    MISC_Cost = db.Column(db.Numeric)
    RMA = db.Column(db.Numeric)
    NGP = db.Column(db.Numeric)
    GP_pre = db.Column(db.Numeric)
    Internal_Transaction_Income = db.Column(db.Numeric)
    Internal_Transaction_Cost = db.Column(db.Numeric)
    OE = db.Column(db.Numeric)
    OE_pre = db.Column(db.Numeric)
    Department_expense_direct_expense = db.Column(db.Numeric)
    Personnel_Related = db.Column(db.Numeric)
    Freight = db.Column(db.Numeric)
    MKT_Channel = db.Column("MKT-Channel", db.Numeric)
    MKT_General = db.Column("MKT-General", db.Numeric)
    RD = db.Column(db.Numeric)
    Depreciation_Amortization = db.Column(db.Numeric)
    Professional_Leagal_fee = db.Column(db.Numeric)
    Business_Trip = db.Column(db.Numeric)
    Rental = db.Column(db.Numeric)
    MISC = db.Column(db.Numeric)
    Commission = db.Column(db.Numeric)
    CH_Platform_cost_Salespre_for_CFT = db.Column(db.Numeric)
    BU_Platform_cost_Salespre_for_BU_LOB = db.Column(db.Numeric)
    Department_expense_indirect_expense = db.Column(db.Numeric)
    Channel_cost_salespre_For_BU = db.Column(db.Numeric)
    RD_salespre_For_CH_CFT = db.Column(db.Numeric)
    Mag_fee_salespre_For_BU_CH = db.Column(db.Numeric)
    OP = db.Column(db.Numeric)
    OIOE = db.Column(db.Numeric)
    Interest_cost = db.Column(db.Numeric)
    PTE = db.Column(db.Numeric)
    NIAC = db.Column(db.Numeric)
    PCE = db.Column(db.Numeric)
    PCE_pre = db.Column(db.Numeric)
    OP_LB_direct = db.Column(db.Numeric)
    PTE_LB_direct = db.Column(db.Numeric)
    PCE_LB_direct = db.Column(db.Numeric)

    def __repr__(self):
        return '<AFPnL %r>' % self.id

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