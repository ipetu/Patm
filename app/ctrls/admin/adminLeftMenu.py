#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/6/2
from app.ctrls.admin import AdminCtrl, admin
from app.dispatcher import AcountLogsModelDispatcher


class Admin_AlogLoginCtrl(AdminCtrl):
    @admin
    def get(self, *args):
        pageSize = 10
        currentPager = self.get_argument('currentPage', default=0, strip=True)
        start = 0
        if currentPager is not 0:
            start = (int(currentPager) - 1) * pageSize
        end = start + pageSize
        prev, next, accountLogs = AcountLogsModelDispatcher.findWithAccountLogPager(start=start, end=end)
        print prev,next
        accountPage = accountLogs.count()
        pageCount = accountPage / pageSize
        if accountPage%pageSize>0:
            pageCount = pageCount+1
        self.render('admin/alog_login.html', accountLogs=accountLogs, prev=prev, next=next, accountPage=accountPage,
                    pageCount=pageCount,currentPager= int(currentPager))
