# -*- coding: utf-8 -*-
# @Time : 2024/1/3 下午 01:14
# @Author : Zendo Chiu (segao)
# @Site :
# @File : UploadFileService.py
# @Software: Pycharm

import random

from model.Users import Users
from model.ACPnL import ACPnL
from model.AFPnL import AFPnL
from utils.ApiResponse import *
from datetime import datetime
import logging
import pandas as pd
import math

logger = logging.getLogger(__name__)

columnNames = ['YYYY', 'MM', 'org0', 'org1', 'org2', 'orgName', 'Revenue', 'COGS', 'GP', 'ImpExp', 'MISC_Cost',
               'RMA', 'NGP', 'GP_pre', 'Internal_Transaction_Income', 'Internal_Transaction_Cost', 'OE',
               'OE_pre', 'Department_expense_direct_expense', 'Personnel_Related', 'Freight', 'MKT-Channel',
               'MKT-General', 'RD', 'Depreciation_Amortization', 'Professional_Leagal_fee', 'Business_Trip',
               'Rental', 'MISC', 'Commission', 'CH_Platform_cost_Salespre_for_CFT',
               'BU_Platform_cost_Salespre_for_BU_LOB', 'Department_expense_indirect_expense',
               'Channel_cost_salespre_For_BU', 'RD_salespre_For_CH_CFT', 'Mag_fee_salespre_For_BU_CH', 'OP',
               'OIOE', 'Interest_cost', 'PTE', 'NIAC', 'PCE', 'PCE_pre', 'OP_LB_direct', 'PTE_LB_direct',
               'PCE_LB_direct']

stringColumn = ['YYYY', 'MM', 'org0', 'org1', 'org2', 'orgName']


# todo add user service

class UploadFileService:
    def upLoadACP(self, data):

        try:
            rows = pd.read_excel(data)
        except:
            rows = pd.read_excel(data)

        totalRow = len(rows)
        for i in range(0, totalRow):
            print(i)
            acpnl = ACPnL()
            rowdata = rows.iloc[i]
            totalColumn = len(rowdata)
            for c in range(0, totalColumn):
                columnName = columnNames[c]
                data = None
                # data = rowdata[columnName]
                if columnName in stringColumn:
                    data = str(rowdata[columnName]) if (
                            ('nan' != str(rowdata[columnName])) or not math.isnan(rowdata[columnName])) else ''
                else:
                    data = rowdata[columnName] if not math.isnan(rowdata[columnName]) else random.randint(1, 10000)
                # data = rowdata[columnName]
                ####get all column name
                # aa = ACPnL.__table__.columns.keys()
                if columnName.find('-'):
                    columnName = columnName.replace('-', '_')
                acpnl.__setattr__(columnName, data)
            acpnl.create(acpnl)
            logger.info("ok")

    def upLoadAFP(self, data):

        try:
            rows = pd.read_excel(data)
        except:
            rows = pd.read_excel(data)

        totalRow = len(rows)
        for i in range(0, totalRow):
            print(i)
            afpnl = AFPnL()
            rowdata = rows.iloc[i]
            totalColumn = len(rowdata)
            for c in range(0, totalColumn):
                columnName = columnNames[c]
                data = None
                if columnName in stringColumn:
                    data = str(rowdata[columnName]) if (
                            ('nan' != str(rowdata[columnName])) or not math.isnan(rowdata[columnName])) else ''
                else:
                    data = rowdata[columnName] if not math.isnan(rowdata[columnName]) else random.randint(1, 10000)
                # data = rowdata[columnName]
                ####get all column name
                # aa = ACPnL.__table__.columns.keys()
                if columnName.find('-'):
                    columnName = columnName.replace('-', '_')
                afpnl.__setattr__(columnName, data)
            afpnl.create(afpnl)
            logger.info("ok")
