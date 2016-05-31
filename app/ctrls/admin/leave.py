# -*- coding: UTF-8 -*-
from app.ctrls.basic import login, BasicCtrl


class LeaveCtrl(BasicCtrl):
    @login
    def get(self):
        self.del_current_sess()
        self.redirect('/admin')
