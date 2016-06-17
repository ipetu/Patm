#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-16 18:19:48
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from tornado.options import options,define
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# mongo_conn_host="192.168.1.155:27017"
# define("mongo_conn_host", mongo_conn_host)
mongo_conn_host="192.168.1.45:27017"
from mongoengine import connect
dbconn = connect('douqu',host=mongo_conn_host)
define("dbconn", dbconn)
# import pymongo
# conn = pymongo.Connection(mongo_conn_host)

#import mongokit
#dbconn = mongokit.Connection(mongo_conn_host)
#define("dbconn", dbconn)
#define("database", "douqu")

# from mongoengine import connect
# dbconn = connect("douqu",mongo_conn_host)
# define("dbconn",dbconn)
#
#
# define("port", default=8090, help="run on the given port", type=int)
# define("api_protocol", default="http")
# define("api_host", default="127.0.0.1")
# define("debug", default=True, type=bool)


# define("mongo_conn", conn)

