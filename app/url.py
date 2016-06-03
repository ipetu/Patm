# -*- coding: UTF-8 -*-
from ctrls.error import ErrorCtrl


from ctrls.admin.three import Admin_ThreeCtrl
from ctrls.admin.second import Admin_SecondCtrl
from ctrls.admin.index import Admin_IndexCtrl
from ctrls.admin.four import Admin_FourCtrl
from ctrls.login import LoginCtrl
from ctrls.admin.leave import LeaveCtrl
from ctrls.index.index import Index_IndexCtrl
from ctrls.admin.adminLeftMenu import Admin_AlogLoginCtrl, Admin_SettingCtrl

url = [
    (r'/admin', Admin_IndexCtrl),
    (r'/second', Admin_SecondCtrl),
    (r'/three', Admin_ThreeCtrl),
    (r'/four', Admin_FourCtrl),
    (r'/alogLogin', Admin_AlogLoginCtrl),
    (r'/setting', Admin_SettingCtrl),
    (r'/login', LoginCtrl),
    (r'/leave', LeaveCtrl),
    (r'/index', Index_IndexCtrl),
    (r'.*', ErrorCtrl)
]
