#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import session_zc

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

from basehandler import BaseHandler

#登陆
class LoginHandler(BaseHandler):
    def get(self,*args,**kwargs):
        self.render("login_page.html")

    def post(self,*args,**kwargs):
        loginemail=self.get_argument('login_email').encode("utf-8")
        loginname=self.get_argument('login_name').encode("utf-8")
        password1=self.get_argument('password1').encode("utf-8")
        print(loginemail,loginname,password1)
        #self.render("query_1.html")

        # %s 要加上'' 否则会出现KeyboardInterrupt的错误
        temp = "select loginemail,loginname,password from userinformation where loginemail='%s' and loginname='%s' and password='%s'" % (loginemail, loginname, password1)
        result = mysql_conn.query(temp)

        if result:
            #if loginname == 'admin' and password1 == 'admin':
            self.set_secure_cookie("user",loginname)
            self.redirect('/')
        else:
            self.write("登录失败！")
            #self.render('login.html',tishi = '用户名或密码错误')