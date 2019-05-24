#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

from basehandler import BaseHandler

class CommentItemHandler(BaseHandler):
	def get(self):
		name = ""
		if self.current_user:
			name = tornado.escape.xhtml_escape(self.current_user) 


		yn = self.get_argument("yn").encode("utf-8")
		info_id = self.get_argument("info_id").encode("utf-8")

		if yn == "y":
			print name + " say this item is skrrrrr!!!"
			sql = "UPDATE infos_comment SET up = up + 1 WHERE info_id=%s;"
			mysql_conn.execute(sql,info_id)
			self.redirect("/item?info_id="+info_id)
		elif yn == "n":
			print name + " say this item is awful!!!"
			sql = "UPDATE infos_comment SET down = down + 1 WHERE info_id=%s;"
	    	mysql_conn.execute(sql,info_id)
	    	self.redirect("/item?info_id="+info_id)