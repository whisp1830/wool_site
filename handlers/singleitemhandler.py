#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

class SingleItemHandler(tornado.web.RequestHandler):
    def get(self):
        info_id = self.get_argument('info_id').encode("utf-8")
        sql = "SELECT * FROM infos WHERE info_id=%s"
        infos = mysql_conn.query(sql,info_id)[0]
        if infos['info_detail']:
            infos['info_detail'] = infos['info_detail'].encode("utf-8").replace("。","。<br>")
        infos['info_tags'] = infos['info_tags'].split(",")[0:3]
        sql = "UPDATE infos SET info_visited = info_visited + 1 WHERE info_id=%s;"
        mysql_conn.execute(sql,info_id)
        self.render('info_detail.html',infos=infos)