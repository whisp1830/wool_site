#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

from basehandler import BaseHandler

class SearchPageHandler(BaseHandler):
    def get(self):
        '''
        返回对应标签的全部内容
        '''

        name = ""
        if self.current_user:
            name = tornado.escape.xhtml_escape(self.current_user) 


        info_tag = self.get_argument('tag').encode("utf-8")
        try:
        	page = int(self.get_argument('page').encode("utf-8"))
        except:
        	page = 1


        start = 20*(page-1)
        end   = 20*page
        infos = None

        brand_en,brand_cn = "",""

        if info_tag[0]=="$":
            info_tag = info_tag[1:]

            print info_tag
            print info_tag
            print info_tag

            if "/" in info_tag:
                brand_en,brand_cn = info_tag.split("/")

            if len(info_tag)<3 or len(brand_cn)<7 or len(brand_en)<3:
                print "放弃FULLTEXT"
                sql = "SELECT * FROM infos WHERE info_tags like '%%%%%s%%%%' ORDER BY info_id DESC LIMIT %s,%s"%(info_tag,start,end)
                infos = mysql_conn.query(sql)

            else:
                print "使用FULLTEXT"
                sql = "SELECT * FROM infos WHERE MATCH(info_tags) AGAINST(%s) ORDER BY info_id DESC LIMIT %s,%s"
                infos = mysql_conn.query(sql,info_tag,start,end)

            self.render('main_page.html',infos=infos,page=page,source="tag",kwd=info_tag,username=name)

        else:
            sql = "SELECT * FROM infos WHERE info_title LIKE '%%%%%s%%%%' ORDER BY info_id DESC LIMIT %s,%s"%(info_tag,start,end)
            infos = mysql_conn.query(sql)
            self.render('main_page.html',infos=infos,page=page,source="search",kwd=info_tag,username=name)


    

    def post(self):
    	'''
		在搜索框中输入内容
    	'''
        name = ""
        if self.current_user:
            name = tornado.escape.xhtml_escape(self.current_user) 
        info_keyword = self.get_argument('info_keyword').encode("utf-8")
        try:
        	page = int(self.get_argument('page').encode("utf-8"))
        except:
        	page = 1
        start = 20*(page-1)
        end   = 20*page        
        sql = "SELECT * FROM infos WHERE info_title LIKE '%%%%%s%%%%' ORDER BY info_id DESC LIMIT %s,%s"%(info_keyword,start,end)
        infos = mysql_conn.query(sql)
        self.render('main_page.html',infos=infos,page=page,source="search",kwd=info_keyword,username=name)