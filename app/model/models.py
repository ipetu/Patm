#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/5/29
"""
 数据库整体结构模块
 1.账号信息表
 2.用户信息表
 3.用户登录日志表
 4.
"""
import datetime

from mongoengine import *


class AccountModel(Document):
    """
    账号信息存储表
    """
    userName = StringField(required=True, unique=True)
    userSalt = StringField()  # 用户校验
    userPerm = IntField(default=0)  # 用户权限
    userPassword = StringField()  # 用户密码
    userMobile = StringField()
    userCtms = DateTimeField(default=datetime.datetime.now, required=True)
    userUtms = DateTimeField(default=datetime.datetime.now, required=True)
    userAtms = DateTimeField(default=datetime.datetime.now, required=True)
    meta = {
        'collection': 'AccountModel',
        'indexes': [{'fields': ['userName'], 'unique': True}]
    }


class UserModel(Document):
    """
    用户个人信息存储表
    """
    userName = StringField(required=True, unique=True)
    # account = ReferenceField(AccountModel,reverse_delete_rule=NULLIFY)#当用户信息被删除的时候,引用对象置为空
    userNick = StringField(max_length=10)
    userMail = StringField()
    userSign = StringField(default='')
    userAvatar = StringField(default='')
    userMeta = StringField(default='')
    userStatus = IntField(default=0)  # 用户是否在线 0不在线 , 1在线
    userCtms = DateTimeField(default=datetime.datetime.now, required=True)
    userUtms = DateTimeField(default=datetime.datetime.now, required=True)
    userAtms = DateTimeField(default=datetime.datetime.now, required=True)
    meta = {
        'collection': 'userModel',
        'indexes': [{'fields': ['userName'], 'unique': True}]
    }

class AcountLogsModel(Document):
    """
    用户登录日志
    """
    alogUserName = StringField(required=True)
    alogUser = ReferenceField(UserModel)
    alogUserIp = StringField()
    alogText = StringField()
    alogData = StringField(default='')
    alogCtms = DateTimeField(default=datetime.datetime.now, required=True)
    meta = {
        'collection': 'AccountLogModel',
        'indexes': [{'fields': ['alogUserName']}]
    }

class PostsModel(Document):
    """
    帖子信息
    """
    postAccount = ReferenceField(AccountModel)
    postTitle = StringField(max_length=20, required=True)
    postDesc = StringField(default='')
    postContent = StringField()
    postSummary = StringField(max_length=50, default='')
    postCtms = DateTimeField(default=datetime.datetime.now, required=True)
    postUtms = DateTimeField(default=datetime.datetime.now, required=True)
    postStart = IntField(default=0)
    meta = {'allow_inheritance': True}
    pass


class VideoPostsModel(PostsModel):
    pass
