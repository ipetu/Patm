#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/5/21

import functools

from app.ctrls.basic import login, BasicCtrl

class AdminCtrl(BasicCtrl):
    pass

def admin(method):
    @login
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.utils('account').chk_user_is_root(self.current_user):
            return method(self, *args, **kwargs)
        else:
            self.flash(0, {'sta': 403, 'url': self.get_login_url()})
            return
    return wrapper

