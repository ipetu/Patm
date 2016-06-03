#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/6/2
from app.ctrls.admin import AdminCtrl, admin
from app.dispatcher import AcountLogsModelDispatcher

"""
系统登录日志
"""
class Admin_AlogLoginCtrl(AdminCtrl):
    @admin
    def get(self, *args):
        """

        :param args:
        :return:
        """
        pageSize = 10
        currentPager = self.get_argument('currentPage', default=0, strip=True)
        start = 0
        if currentPager is not 0:
            start = (int(currentPager) - 1) * pageSize
        end = start + pageSize
        prev, next, accountLogs = AcountLogsModelDispatcher.findWithAccountLogPager(start=start, end=end)
        accountPage = accountLogs.count()
        pageCount = accountPage / pageSize
        if accountPage%pageSize>0:
            pageCount = pageCount+1
        self.render('admin/alog_login.html', accountLogs=accountLogs, prev=prev, next=next, accountPage=accountPage,
                    pageCount=pageCount,currentPager= int(currentPager))

"""
系统设置
"""
class Admin_SettingCtrl(AdminCtrl):
    @admin
    def get(self, *args):
        self.render('admin/setting.html')
