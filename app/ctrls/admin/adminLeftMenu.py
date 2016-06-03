#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/6/2
from app.ctrls.admin import AdminCtrl, admin
from app.dispatcher import AcountLogsModelDispatcher


class Admin_AlogLoginCtrl(AdminCtrl):
    @admin
    def get(self, *args):
        limit = 5
        arguments = self.request.arguments
        if arguments is not None and len(arguments)>0:
            self.write('hello')
            pass
        else:
            accountLogs = AcountLogsModelDispatcher.findWithAllAccountLog(limit)
            accountPage = accountLogs.count()
            pageCount = accountPage / limit
            self.render('admin/alog_login.html', accountLogs=accountLogs, accountPage=accountPage, pageCount=pageCount)


