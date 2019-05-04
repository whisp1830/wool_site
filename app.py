#-*- coding: utf-8 -*-
import os.path

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import datetime
mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
define("port", default=8000, help="run on the given port", type=int)

class MainPageHandler(tornado.web.RequestHandler):
    def get(self):
        sql = "SELECT * FROM infos ORDER BY info_update_time DESC LIMIT 200"
        infos = mysql_conn.query(sql)
        self.render('main.html',infos=infos)

class SearchPageHandler(tornado.web.RequestHandler):
    def post(self):
        info_keyword = self.get_argument('info_keyword').encode("utf-8")
        sql = "SELECT * FROM infos WHERE info_title LIKE '%%%%%s%%%%'"%info_keyword
        infos = mysql_conn.query(sql)
        self.render('main.html',infos=infos)

class SingleItemHandler(tornado.web.RequestHandler):
    def get(self):
        info_id = self.get_argument('info_id').encode("utf-8")
        sql = "SELECT * FROM infos WHERE info_id=%s"
        infos = mysql_conn.query(sql,info_id)[0]
        if infos['info_detail']:
            infos['info_detail'] = infos['info_detail'].encode("utf-8").replace("。","。<br>")

        sql = "UPDATE infos SET info_visited = info_visited + 1 WHERE info_id=%s;"
        mysql_conn.execute(sql,info_id)
        self.render('info_detail.html',infos=infos)
    def post(self):
        pass


class PostInfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('po.html')

    def post(self):
        info_title = self.get_argument('info_title').encode("utf-8")
        info_price = self.get_argument('info_price').encode("utf-8")
        info_detail = self.get_argument('info_detail').encode("utf-8")
        label_usage = self.get_argument('label_usage').encode("utf-8")

        sql = "INSERT INTO infos(info_title,info_price,info_detail,label_usage)"\
                "VALUES (%s,%s,%s,%s)"
        mysql_conn.execute(sql,info_title,info_price,info_detail,label_usage)

        self.redirect("/all")


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/po', PostInfoHandler),
                  (r'/',MainPageHandler),
                  (r'/item',SingleItemHandler),
                  (r'/search',SearchPageHandler)],
        template_path=os.path.join(os.path.dirname(__file__),"templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()