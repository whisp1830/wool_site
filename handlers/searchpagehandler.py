#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

class SearchPageHandler(tornado.web.RequestHandler):
    def post(self):
        info_keyword = self.get_argument('info_keyword').encode("utf-8")
        sql = "SELECT * FROM infos WHERE info_title LIKE '%%%%%s%%%%' ORDER BY info_id DESC"%info_keyword
        infos = mysql_conn.query(sql)
        self.render('main.html',infos=infos)