#encoding:utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

#注册
class SignHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("signin_page.html")

    def post(self,*args,**kwargs):
        loginemail=self.get_argument('login_email').encode("utf-8")
        loginname=self.get_argument("login_name").encode("utf-8")
        password1=self.get_argument('password1').encode("utf-8")
        password2=self.get_argument('password2').encode("utf-8")

        # %s 要加上'' 否则会出现KeyboardInterrupt的错误
        temp1 = "select loginemail,loginname from userinformation where loginemail='%s' or loginname='%s'" % (loginemail, loginname)
        result1 = mysql_conn.query(temp1)
        if result1:
            self.write('邮箱已注册或者用户名已存在！')
        else:
            if password1==password2:
                try:
                    #执行语句
                    temp2 = "insert into userinformation(loginemail,loginname,password) values(%s,%s,%s)"
                except Exception as e:
                    print(str(e))
                mysql_conn.execute(temp2, loginemail, loginname, password1)


                self.redirect("/login")
            else:
                self.write("两次密码不相同！")