#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/5/21
from . import admin, AdminCtrl

class Admin_SecondCtrl(AdminCtrl):
    def get(self, *args):
        Alists = self.model('alist').getAll(10)
        self.render('admin/second.html',Alist = Alists)