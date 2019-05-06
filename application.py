# coding=utf-8
"""
定义应用
"""
import tornado.web

from settings import SETTINGS
from urls import urls


class Application(tornado.web.Application):

    def __init__(self):
        handlers = urls
        settings = SETTINGS
        tornado.web.Application.__init__(self, handlers, **settings)
