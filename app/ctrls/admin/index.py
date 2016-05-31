# -*- coding: UTF-8 -*-

from . import admin, AdminCtrl

class Admin_IndexCtrl(AdminCtrl):
    @admin
    def get(self, *args):

        self.render('admin/index.html')

