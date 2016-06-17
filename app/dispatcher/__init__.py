#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/5/29
from app.model.models import (AccountModel, UserModel, AcountLogsModel, PostsModel, VideoPostsModel, SystemSettingModel)

"""
账号信息操作类
"""
class AccountModelDispatcher(object):
    @staticmethod
    def saveAccountInfo(userName, userSalt, userPassword, userMobile=''):
        """
        保存账号信息
        :rtype: object
        :param userNick:
        :param userSalt:
        :param userPassword:
        :param userMobile:
        :return:
        """
        accountModel = AccountModel()
        accountModel.userName = userName
        accountModel.userSalt = userSalt
        accountModel.userPassword = userPassword
        accountModel.userMobile = userMobile
        return accountModel.save()

    @staticmethod
    def findWithAccountUserName(userName):
        """
        通过userName查询出对应的信息
        :param userName:
        :return:
        """
        return AccountModel.objects(userName=userName).first()

    @staticmethod
    def _findWithAccountObjectId(id):
        """
        通过userName查询出对应的信息
        :param _id:
        :return:
        """
        from bson import ObjectId
        return AccountModel.objects(id=ObjectId(id)).first()

"""
个人信息操作类
"""
class UserModelDispatcher(object):
    @staticmethod
    def saveUserInfo(userName, userNick, userAvatar, userSign='', userMail='', userMeta='', userStatus=1):
        """
        保存用户个人信息
        :param account:
        :param userNick:
        :param userAvatar:
        :param userSign:
        :param userMail:
        :param userMeta:
        :param userStatus:
        :return:
        """
        userModel = UserModel()
        userModel.userName = userName
        # userModel.account = account
        userModel.userAvatar = userAvatar
        userModel.userNick = userNick
        userModel.userSign = userSign
        userModel.userMail = userMail
        userModel.userMeta = userMeta
        userModel.userStatus = userStatus
        return userModel.save()

    @staticmethod
    def findWithUsername(username):
        """
        通过userName查询出个人信息
        :param self:
        :param userName:
        :return:
        """
        return UserModel.objects(userName=username).first()

    @staticmethod
    def findWithUserNick(userNick):
        """
        通过userName查询出个人信息
        :param self:
        :param userNick:
        :return:
        """
        return UserModel.objects(userNick=userNick).first()

    @staticmethod
    def deleteWithUsername(username):
        """
        如果查询的用户存在,则删除该用户
        :param self:
        :param username:
        :return:
        """
        userInfo = UserModelDispatcher.findWithUsername(username)
        if userInfo is not None:
            return userInfo.delete()
        return None

    @staticmethod
    def updateWithUserName(username):
        pass

"""
账号登录日志操作
"""
class AcountLogsModelDispatcher(object):
    @staticmethod
    def saveLog(username, user, text, userIp, userData=''):
        """
        保存用户的登陆信息
        :param username:
        :param user:
        :param text:
        :param userIp:
        :param alogData:
        :return:
        """
        accountLog = AcountLogsModel()
        accountLog.alogUserName = username
        accountLog.alogUser = user
        accountLog.alogText = text
        accountLog.alogUserIp = userIp
        accountLog.alogData = userData
        return accountLog.save()

    @staticmethod
    def findWithAccountLogPager(start=0, end=5, order='-alogCtms', limit=10):
        size = end - start
        prev = next = False
        accountLogs = AcountLogsModel.objects.order_by(order)[start:end + 1]
        if len(accountLogs) - size > 0:
            next = True
        if start != 0:
            prev = True
        return prev, next, accountLogs[start:end]

"""
系统相关的设置操作
"""
class SystemSettingModelDispatcher(object):

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.findWithAllSystemSetting()

    def findWithAllSystemSetting(self):
        """
        查询数据库中全部的系统设置,并把它缓存到内存中
        :return:
        """
        self._cache = {}
        ret = SystemSettingModel.objects
        if ret:
            for row in ret:
                self._cache[row['systemSettingName']] = row['systemSettingValue']

    def obtain(self,name):
        """
        检测这个key是否在缓存中,如果不在缓存中,则去db中查询
        :param name:
        :return:
        """
        if name not in self._cache:
            ret = SystemSettingModel.objects.first()
            if ret:
                self._cache[name] = ret['systemSettingValue']
            else:
                self._cache[name] = None
        return self._cache[name]

    def updateSetting(self,settingName='', settingValue=''):
        """
        更新系统设置
        :param settingName:
        :param settingValue:
        :return:
        """
        setting = SystemSettingModel.objects(systemSettingName=settingName).first()
        if setting is not None:
            setting.systemSettingValue = settingValue
            return setting.save()
        return False

    def deleteWithSystemSettingName(self,systemSettingName):
        singleSystemSetting = SystemSettingModel.objects(systemSettingName=systemSettingName).first()
        if singleSystemSetting is not None:
            singleSystemSetting.delete()
        self._cache[systemSettingName] = None

    @staticmethod
    def findWithSystemSettingPager(start=0, end=5, order='-settingCtms', limit=10):
        """
        分页查找系统设置
        :param start:
        :param end:
        :param order:
        :param limit:
        :return:
        """
        size = end - start
        prev = next = False
        systemSettings = SystemSettingModel.objects.order_by(order)[start:end + 1]
        if len(systemSettings) - size > 0:
            next = True
        if start != 0:
            prev = True
        return prev, next, systemSettings[start:end]

    @staticmethod
    def saveSetting(settingName='', settingValue=''):
        """
        保存系统设置
        :param settingName:
        :param settingValue:
        :return:
        """
        systemSetting = SystemSettingModel()
        systemSetting.systemSettingName = settingName
        systemSetting.systemSettingValue = settingValue
        return systemSetting.save()

    @staticmethod
    def findWithSettingName(settingName=''):
        """

        :param settingName:
        :return:
        """
        return SystemSettingModel.objects(systemSettingName=settingName).first()
