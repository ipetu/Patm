# -*- coding: UTF-8 -*-

import os, re
import sqlite3
from collections import OrderedDict

class Datum(object):
    def __init__(self, config):
        # super(self.__class__, self).__init__(config)
        self.config = {'path': '', 'form': '.sdb'}
        self.config.update(config)

        self.source = sqlite3.connect(self.locate(self.config['path'], self.config['form']))
        self.source.row_factory = self.__class__.sqlite_dict # sqlite3.Row
        self.source.text_factory = str

    def locate(self, path = '', form = ''):
        return path + os.path.join(*re.sub(r'Datum$', '', self.__class__.__name__).lower().split('_')) + form

    def cursor(self, *args, **kwargs):
        return self.source.cursor(*args, **kwargs)

    def commit(self, *args, **kwargs):
        return self.source.commit(*args, **kwargs)

    def revert(self, *args, **kwargs):
        return self.source.rollback(*args, **kwargs)

    def result(self, *args, **kwargs):
        cur = self.source.cursor()
        cur.execute(*args, **kwargs)
        ret = cur.fetchall()
        cur.close()
        return ret

    def single(self, *args, **kwargs):
        cur = self.source.cursor()
        cur.execute(*args, **kwargs)
        ret = cur.fetchone()
        cur.close()
        return ret

    def invoke(self, *args, **kwargs):
        return self.source.execute(*args, **kwargs)

    def affect(self, *args, **kwargs):
        con = self.source
        cur = con.execute(*args, **kwargs)
        con.commit()
        return cur

    @staticmethod
    def sqlite_dict(cur, row):
        return OrderedDict((v[0], row[i]) for i, v in enumerate(cur.description))

    @staticmethod
    def sqlite_rows(cur):
        return [OrderedDict((v[0], row[i if i in row else v[0]]) for i, v in enumerate(cur.description)) for row in cur.fetchall()]

