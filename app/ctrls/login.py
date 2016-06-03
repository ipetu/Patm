# -*- coding: UTF-8 -*-
from basic import BasicCtrl
from app.dispatcher import (UserModelDispatcher,AccountModelDispatcher)

class LoginCtrl(BasicCtrl):
    def get(self):
        self.render('login.html', next = self.input('next', '/shell'))

    def post(self):
        # if not self.human_valid():
        #     self.flash(0, {'msg': '验证码错误'})
        #     return

        try:
            userNick = self.input('username')
            password = self.input('password')
            remember = self.input('remember', None)
            redirect = self.input('redirect', '/shell')
            #
            if remember:
                remember = int(remember)

            userModel = UserModelDispatcher.findWithUserNick(userNick=userNick)
            if userModel is not None:
                userName = userModel['userName']
                accountModel = AccountModelDispatcher.findWithAccountUserName(userName)
                # if accountModel and self.entry('login:user#' + str(accountModel['userName'])):
                #     self.flash(0, {'msg': '操作太频繁，请稍后再试', 'sta': 429})
                #     return

                if accountModel and self.utils('account').generate_password(password, accountModel['userSalt']) == accountModel['userPassword']:
                    self.set_current_sess(accountModel, days=remember)

                    self.ualog(userModel, '后台登录')
                    self.flash(1, {'url': redirect})
                    return
        except Exception,e:
            print e

        self.flash(0, {'msg': '用户名或密码错误','url':redirect})
