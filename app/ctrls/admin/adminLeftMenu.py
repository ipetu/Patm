#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/6/2
from app.ctrls.admin import AdminCtrl, admin
from app.dispatcher import AcountLogsModelDispatcher, SystemSettingModelDispatcher, UserModelDispatcher

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
        if accountPage % pageSize > 0:
            pageCount = pageCount + 1
        self.render('admin/alog_login.html', accountLogs=accountLogs, prev=prev, next=next, accountPage=accountPage,
                    pageCount=pageCount, currentPager=int(currentPager))


class Admin_SettingCtrl(AdminCtrl):
    @admin
    def get(self, *args):
        """
        获取系统设置
        :param args:
        :return:
        """
        # SystemSettingModelDispatcher.saveSetting(settingName='descp',settingValue='descp')
        # SystemSettingModelDispatcher.saveSetting(settingName='keyws',settingValue='keyws')
        # SystemSettingModelDispatcher.saveSetting(settingName='title',settingValue='title')
        # SystemSettingModelDispatcher.saveSetting(settingName='topic',settingValue='topic')
        # SystemSettingModelDispatcher.saveSetting(settingName='brand',settingValue='brand')
        # SystemSettingModelDispatcher.saveSetting(settingName='built',settingValue='built')
        # SystemSettingModelDispatcher.saveSetting(settingName='power',settingValue='power')
        pageSize = 5
        currentPager = self.get_argument('currentPage', default=0, strip=True)
        start = 0
        if currentPager is not 0:
            start = (int(currentPager) - 1) * pageSize
        end = start + pageSize
        prev, next, systemSettings = SystemSettingModelDispatcher.findWithSystemSettingPager(start=start, end=end)
        accountPage = systemSettings.count()
        pageCount = accountPage / pageSize
        if accountPage % pageSize > 0:
            pageCount = pageCount + 1
        self.render('admin/setting.html', systemSettings=systemSettings, prev=prev, next=next, accountPage=accountPage,
                    pageCount=pageCount, currentPager=int(currentPager))

class Admin_SettingEditCtrl(AdminCtrl):
    @admin
    def get(self, *args):
        """
        系统设置修改

        :param args:
        :return:
        """
        editSetting = self.get_argument('edit', default='', strip=True)
        editSettingModel = SystemSettingModelDispatcher.findWithSettingName(editSetting)
        if not editSettingModel:
            self.flash(0, {'sta': 404})
            return
        self.render('admin/setting_edit.html',editSettingModel=editSettingModel)
    @admin
    def post(self, *args, **kwargs):
        try:
            settingName = self.get_argument('conf_name', default='', strip=True)
            settingValue = self.get_argument('conf_vals', default='', strip=True)
            settingModel = SystemSettingModelDispatcher()
            #todu 这里需要做判断是否修改成功
            settingModel.updateSetting(settingName=settingName,settingValue=settingValue)
            userName = self.current_user.userName
            userModel = UserModelDispatcher.findWithUsername(username=userName)
            self.ualog(userModel, "修改配置成功：" + settingName, settingValue)
            self.flash(1,{'msg':'更新配置成功'})
        except Exception,e:
            self.flash(0)

"""
增加系统设置
"""


class Admin_SettingCreateCtrl(AdminCtrl):
    @admin
    def get(self, *args):
        """
        增加系统设置
        :param args:
        :return:
        """
        self.render('admin/setting_create.html')

    @admin
    def post(self, *args, **kwargs):
        """
            增加系统设置
            :param args:
            :return:
            """
        self.render('admin/setting_create.html')


class Admin_SettingDeleteCtrl(AdminCtrl):
    @admin
    def post(self, *args, **kwargs):
        try:
            systemSettingName = self.input('systemSettingName')
            conf_vals = self.get_runtime_conf(systemSettingName)
            SystemSettingModelDispatcher().deleteWithSystemSettingName(systemSettingName=systemSettingName)
            userName = self.current_user.userName
            userModel = UserModelDispatcher.findWithUsername(username=userName)
            self.ualog(userModel, "删除配置：" + systemSettingName, conf_vals)
            self.flash(1, {'msg': '删除配置成功'})
        except Exception ,e:
            self.flash(0)
