#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Liuwf on 16/5/21
from . import admin, AdminCtrl

class Admin_FourCtrl(AdminCtrl):
    def get(self, *args):
        self.render('admin/four.html')