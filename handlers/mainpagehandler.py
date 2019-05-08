#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

class MainPageHandler(tornado.web.RequestHandler):
    def get(self):
        sql = "SELECT * FROM infos ORDER BY info_id DESC LIMIT 100"
        infos = mysql_conn.query(sql)

        self.render('main.html',infos=infos)