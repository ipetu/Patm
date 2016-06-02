#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/6/2
from app.ctrls.admin import AdminCtrl, admin
from app.dispatcher import AcountLogsModelDispatcher


class Admin_AlogLoginCtrl(AdminCtrl):
    @admin
    def get(self, *args):
        accountLogs = AcountLogsModelDispatcher.findWithAllAccountLog()
        # for index,i in accountLogs:
        #     print index,i
        # for index in range(len(accountLogs)):
        #     print index
        #     print accountLogs[index]
        self.render('admin/alog_login.html',accountLogs = accountLogs)