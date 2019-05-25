#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

from basehandler import BaseHandler

class RankPageHandler(BaseHandler):
    def get(self,data):

		name = ""
		print self.current_user
		if self.current_user:
		    name = tornado.escape.xhtml_escape(self.current_user) 

		data = data.encode("utf-8")
		if data == "cabbage":
			kwd = "每日白菜"
			sql = "SELECT * FROM infos WHERE MATCH(info_tags) AGAINST(%s) ORDER BY info_update_time DESC LIMIT 40"
			infos = mysql_conn.query(sql,kwd)
			self.render("rank_page.html",infos=infos,page=1,source="rank",username=name)

		if data == "viewed":
			kwd = "当前热门"
			sql = "SELECT * FROM infos,infos_comment WHERE infos.info_id = infos_comment.info_id"\
					" ORDER BY info_visited DESC LIMIT 40"
			infos = mysql_conn.query(sql)
			self.render("rank_page.html",infos=infos,page=1,source="rank",username=name)

		if data == "best":
			kwd = "最受好评"
			sql = "SELECT * FROM infos,infos_comment WHERE infos.info_id = infos_comment.info_id"\
					" ORDER BY infos_comment.up-infos_comment.down DESC LIMIT 40"
			infos = mysql_conn.query(sql)
			self.render("rank_page.html",infos=infos,page=1,source="rank",username=name)

		if data == "worst":
			kwd = "风评被害"
			sql = "SELECT * FROM infos,infos_comment WHERE infos.info_id = infos_comment.info_id"\
					" ORDER BY infos_comment.up-infos_comment.down ASC LIMIT 40"
			infos = mysql_conn.query(sql)
			self.render("rank_page.html",infos=infos,page=1,source="rank",username=name)

		if data == "global":
			kwd = "海淘精选"
			sql = "SELECT * FROM infos WHERE MATCH(info_tags) AGAINST(%s) ORDER BY info_update_time DESC LIMIT 40"
			infos = mysql_conn.query(sql,kwd)
			self.render("rank_page.html",infos=infos,page=1,source="rank",username=name)


		else:
			kwd = "最受好评"
			sql = "SELECT * FROM infos,infos_comment WHERE infos.info_id = infos_comment.info_id"\
					" ORDER BY infos_comment.up-infos_comment.down DESC LIMIT 40"
			infos = mysql_conn.query(sql)
			self.render("rank_page.html",infos=infos,page=1,source="rank",username=name)



