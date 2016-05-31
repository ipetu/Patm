#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/5/29
from app.model.models import (AccountModel, UserModel, AcountLogsModel, PostsModel, VideoPostsModel)


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
