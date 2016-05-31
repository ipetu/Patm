# -*- coding: UTF-8 -*-

import sys


reload(sys)

import os.path

sys.setdefaultencoding('utf-8')
sys.path[0] = os.path.dirname(sys.path[0])
sys.path.insert(1, os.path.join(sys.path[0], 'lib'))

import tornado.web
import tornado.ioloop
from tornado.options import define, options

from app.url import url
from app.etc import etc
svr = tornado.web.Application(handlers = url, **etc)
from app import dbConfig
define("port", default=8001, help="run on the given port", type=int)
def main():
    options.parse_command_line()
    print("Starting tornado web server on http://127.0.0.1:%s" % options.port)
    print("Quit the server with CONTROL-C")
    svr.listen(options.port, xheaders=True)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
