# -*- coding: UTF-8 -*-
from ctrls.error import ErrorCtrl


from ctrls.admin.index import Admin_IndexCtrl
from ctrls.login import LoginCtrl
from ctrls.admin.leave import LeaveCtrl
from ctrls.index.index import Index_IndexCtrl
from ctrls.admin.adminLeftMenu import Admin_AlogLoginCtrl, Admin_SettingCtrl, Admin_SettingCreateCtrl, \
    Admin_SettingDeleteCtrl, Admin_SettingEditCtrl, Admin_LinkCtrl

url = [
    (r'/admin', Admin_IndexCtrl),
    (r'/admin/alogLogin', Admin_AlogLoginCtrl),
    (r'/admin/link', Admin_LinkCtrl),
    (r'/admin/link_create', Admin_LinkCtrl),
    (r'/admin/setting', Admin_SettingCtrl),
    (r'/admin/setting_edit', Admin_SettingEditCtrl),
    (r'/admin/setting_create', Admin_SettingCreateCtrl),
    (r'/admin/setting_delete', Admin_SettingDeleteCtrl),
    (r'/login', LoginCtrl),
    (r'/leave', LeaveCtrl),
    (r'/index', Index_IndexCtrl),
    (r'.*', ErrorCtrl)
]
