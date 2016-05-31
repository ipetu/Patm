# -*- coding: UTF-8 -*-

import time
import re

class Cache:
    _ = {}

    @staticmethod
    def obtain(key):
        if key in Cache._:
            try:
                if 'v' in Cache._[key] and 'e' in Cache._[key] and (Cache._[key]['e'] is None or Cache._[key]['e'] > int(time.time())):
                    return Cache._[key]['v']
                Cache.delete(key)
            except:
                pass

    @staticmethod
    def upsert(key, val, lft = 3600):
        Cache._[key] = {'v': val, 'e': None if lft is None else (int(time.time()) + int(lft))}

    @staticmethod
    def delete(key, exp = False):
        try:
            if exp:
                for k in Cache._:
                    if re.search(key, k):
                        del Cache._[k]
            elif (key in Cache._):
                del Cache._[key]
        except:
            pass
