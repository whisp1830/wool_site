#encoding:utf-8
import random
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

from basehandler import BaseHandler

class SingleItemHandler(BaseHandler):

    def get_recommends(self,sql_param):
        '''
        根据当前优惠信息，推荐更多相似优惠信息
        '''
        sql = 'SELECT * FROM infos WHERE MATCH(info_tags) AGAINST(%s) UNION '\
                'SELECT * FROM infos WHERE MATCH(info_tags) AGAINST(%s) UNION '\
                'SELECT * FROM infos WHERE MATCH(info_tags) AGAINST(%s)\
                LIMIT 8;'

        recommends = mysql_conn.query(sql,sql_param[2],sql_param[1],sql_param[0])

        return recommends


    def get_top(self):
        '''
        推荐最热门的优惠信息
        '''
        sql = 'SELECT * FROM infos,infos_comment WHERE infos.info_id=infos_comment.info_id\
                 ORDER BY info_visited DESC LIMIT 5'

        top = mysql_conn.query(sql)

        return top

    def update_visited_count(self,info_id):
        '''
        每次有用户访问优惠信息页面，给对应记录的info_visited字段加一
        '''
        add_visited = random.randint(1,500)
        sql = "UPDATE infos_comment SET info_visited = info_visited + %s WHERE info_id=%s;"
        mysql_conn.execute(sql,str(add_visited),info_id)


    def get_up_and_down(self,info_id):
        '''
        返回用户点赞，点踩的人数
        '''
        sql = "SELECT up,down FROM infos_comment WHERE info_id=%s"
        up_down = mysql_conn.query(sql,info_id)

        return up_down


    def get(self):
        '''
        返回单个优惠信息页面的全部内容
        '''
        name = ""
        if self.current_user:
            name = tornado.escape.xhtml_escape(self.current_user) 

        info_id = self.get_argument('info_id').encode("utf-8")
        sql = "SELECT * FROM infos,infos_comment WHERE infos.info_id=%s and \
                infos.info_id=infos_comment.info_id"

        infos = mysql_conn.query(sql,info_id)[0]
        if infos['info_detail']:
            infos['info_detail'] = infos['info_detail'].encode("utf-8").replace("。","。<br>")
        infos['info_tags'] = infos['info_tags'].split(",")[0:3]


        top = self.get_top()
        recommends = self.get_recommends(infos['info_tags'])
        up_and_down = self.get_up_and_down(info_id)[0]
        self.update_visited_count(info_id)
        
        print up_and_down
        print up_and_down
        print up_and_down        

        self.render('detail_page.html',infos=infos,recommends=recommends,top=top,up_down=up_and_down,username=name)

    def post(self):
        a = self.get_arguments(name="reason")

        sql = "INSERT INTO report_history()"

        self.write("chexked")
        
        