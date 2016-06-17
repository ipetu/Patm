#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/6/2
from app.ctrls.admin import AdminCtrl, admin
from app.dispatcher import AcountLogsModelDispatcher, SystemSettingModelDispatcher, UserModelDispatcher, \
    LinksModelDispatcher

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
        self.render('admin/setting_edit.html', editSettingModel=editSettingModel)

    @admin
    def post(self, *args, **kwargs):
        try:
            settingName = self.get_argument('conf_name', default='', strip=True)
            settingValue = self.get_argument('conf_vals', default='', strip=True)
            settingModel = SystemSettingModelDispatcher()
            # todu 这里需要做判断是否修改成功
            settingModel.updateSetting(settingName=settingName, settingValue=settingValue)
            userName = self.current_user.userName
            userModel = UserModelDispatcher.findWithUsername(username=userName)
            self.ualog(userModel, "修改配置成功：" + settingName, settingValue)
            self.flash(1, {'msg': '更新配置成功'})
        except:
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
        try:
            settingName = self.get_argument('conf_name', default='', strip=True)
            settingValue = self.get_argument('conf_vals', default='', strip=True)
            if len(settingName) > 32:
                self.flash(0, {'msg': '配置键长度不能超过32个字符'})
                return
            settingModel = SystemSettingModelDispatcher.findWithSettingName(settingName=settingName)
            if settingModel is not None:
                self.flash(0, {'msg': '配置键已存在'})
                return
            SystemSettingModelDispatcher.saveSetting(settingName=settingName, settingValue=settingValue)
            userName = self.current_user.userName
            userModel = UserModelDispatcher.findWithUsername(username=userName)
            self.ualog(userModel, "增加配置成功：" + settingName, settingValue)
            self.flash(1, {'msg': '增加配置成功'})
        except:
            self.flash(0)


class Admin_SettingDeleteCtrl(AdminCtrl):
    @admin
    def post(self, *args, **kwargs):
        """
        删除系统设置
        :param args:
        :param kwargs:
        :return:
        """
        try:
            systemSettingName = self.input('systemSettingName')
            conf_vals = self.get_runtime_conf(systemSettingName)
            SystemSettingModelDispatcher().deleteWithSystemSettingName(systemSettingName=systemSettingName)
            userName = self.current_user.userName
            userModel = UserModelDispatcher.findWithUsername(username=userName)
            self.ualog(userModel, "删除配置：" + systemSettingName, conf_vals)
            self.flash(1, {'msg': '删除配置成功'})
        except:
            self.flash(0)


"""
链接列表
"""


class Admin_LinkCtrl(AdminCtrl):
    @admin
    def get(self, *args):
        """
        链接列表
        :param args:
        :return:
        """
        pageSize = 10
        currentPager = self.get_argument('currentPage', default=0, strip=True)
        start = 0
        if currentPager is not 0:
            start = (int(currentPager) - 1) * pageSize
        end = start + pageSize
        prev, next, linkModels = LinksModelDispatcher.findWithLinkPager(start=start, end=end)
        linkPage = linkModels.count()
        pageCount = linkPage / pageSize
        if linkPage % pageSize > 0:
            pageCount = pageCount + 1
        self.render('admin/link.html', linkModels=linkModels, prev=prev, next=next, linkPage=linkPage,
                    pageCount=pageCount, currentPager=int(currentPager))


"""
链接创建
"""


class Admin_LinkCreateCtrl(AdminCtrl):
    @admin
    def get(self, *args):
        """
        链接创建
        :param args:
        :return:
        """
        self.render('admin/link_create.html')

    @admin
    def post(self, *args, **kwargs):
        """
            链接创建
            :param args:
            :return:
            """
        try:
            linkAddress = self.get_argument('link_address', default='', strip=True)
            linkTitle = self.get_argument('link_title', default='', strip=True)
            linkDesc = self.get_argument('link_desc', default='', strip=True)
            linkScore = self.get_argument('link_score', default='', strip=True)
            linkModel = LinksModelDispatcher.findWithLinkAddress(lkAddress=linkAddress)
            if linkModel is not None:
                self.flash(0, {'msg': '该网址已经存在'})
                return
            LinksModelDispatcher.saveLinks(lkAddress=linkAddress, lkTitle=linkTitle, lkDesc=linkDesc, lkScore=linkScore)
            userName = self.current_user.userName
            userModel = UserModelDispatcher.findWithUsername(username=userName)
            self.ualog(userModel, "增加链接地址成功：" + linkAddress, linkDesc)
            self.flash(1, {'msg': '增加链接地址成功'})
        except:
            self.flash(0)


"""
链接删除
"""


class Admin_LinkDeleteCtrl(AdminCtrl):
    @admin
    def post(self, *args, **kwargs):
        """
        链接删除
        :param args:
        :param kwargs:
        :return:
        """
        try:
            linkAddress = self.input('linkAddress')
            result = LinksModelDispatcher.deleteWithLinkAddressName(lkAddress=linkAddress)
            if result :
                userName = self.current_user.userName
                userModel = UserModelDispatcher.findWithUsername(username=userName)
                self.ualog(userModel, "删除链接：" + linkAddress, linkAddress)
                self.flash(1, {'msg': '删除链接成功'})
            else:
                self.flash(0,{'msg':'删除失败'})
        except:
            self.flash(0)

class Admin_LinkEditCtrl(AdminCtrl):
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
        self.render('admin/link_edit.html', editSettingModel=editSettingModel)

    @admin
    def post(self, *args, **kwargs):
        try:
            settingName = self.get_argument('conf_name', default='', strip=True)
            settingValue = self.get_argument('conf_vals', default='', strip=True)
            settingModel = SystemSettingModelDispatcher()
            # todu 这里需要做判断是否修改成功
            settingModel.updateSetting(settingName=settingName, settingValue=settingValue)
            userName = self.current_user.userName
            userModel = UserModelDispatcher.findWithUsername(username=userName)
            self.ualog(userModel, "修改配置成功：" + settingName, settingValue)
            self.flash(1, {'msg': '更新配置成功'})
        except:
            self.flash(0)
