#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/5/21
from . import admin, AdminCtrl

class Admin_SecondCtrl(AdminCtrl):
    @admin
    def get(self, *args):
        pass
        # Alists = self.model('alist').getAll(10)
        # self.render('admin/second.html',Alist = Alists)