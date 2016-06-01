# -*- coding: UTF-8 -*-
from tornado.options import options

from app.ctrls.basic import BasicCtrl
from app.dispatcher import (AccountModelDispatcher, UserModelDispatcher)

class Index_IndexCtrl(BasicCtrl):
    def get(self, *args):
        # self.saveUserInfo()
        self.render('index/index.html')

    def saveUserInfo(self):

        # if True:
        for index in range(1):
            userName = self.utils('account').generate_username();
            passwrod = self.utils('account').generate_password('123456', 'asdflkjh')
            userNick = "admin"
            userAvatar = "http://qcloud.dpfile.com/pc/X7UcuoYuamFwCQTtNO6WTFf4jEat2raHUMPSaOT7TLGhLC5f0SSJr4dqexDFSz-STYGVDmosZWTLal1WbWRW3A.jpg"
            userSign = "就是这么屌啊"
            userMail = "hello" + str(index) + "@gmail.com"
            AccountModelDispatcher.saveAccountInfo(userName=userName, userSalt='asdflkjh',
                                                                 userPassword=passwrod)
            UserModelDispatcher.saveUserInfo(userName=userName,userNick=userNick,
                                             userAvatar=userAvatar, userSign=userSign, userMail=userMail)

        # obj = UserModelDispatcher.findWithUsername(self,'9e9eeee1266f11e6a32080e65012da4c')
        # print type(obj)
        # print type(obj['account'])






