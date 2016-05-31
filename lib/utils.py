# -*- coding: UTF-8 -*-

import re
import hashlib

class Utils:
    @staticmethod
    def array_keyto(ary, key):
        ret = {}
        for val in ary:
            ret[val[key]] = val
        return ret

    @staticmethod
    def array_group(ary, key):
        ret = {}
        for val in ary:
            if val[key] not in ret:
                ret[val[key]] = []
            ret[val[key]].append(val)
        return ret

    @staticmethod
    def array_field(ary, key):
        ret = []
        for val in ary:
            ret.append(val[key])
        return ret

    @staticmethod
    def build_links(val, opt = ' target="_blank"'):
        exp = re.compile(
                r'('
                r'(?:http|ftp)s?://'           # http:// or https://
                r'[a-z0-9-]+(?:\.[a-z0-9-]+)*' # domain or ip...
                r'(?::\d+)?'                   # optional port
                r'(?:/[^"\'<>\s]*)?'           # optional segs
                r')', re.IGNORECASE)
        return exp.sub(r'<a href="\1"' + opt + r'>\1</a>', val)

    @staticmethod
    def str_md5_hex(val):
        return hashlib.md5(val).hexdigest()
