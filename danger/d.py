import os
import torndb
mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")
images = mysql_conn.query("select info_image from infos;")

for i in images:
    if i['info_image']:
    	yuju = "curl "+" -o "+str(i['info_image']).split("/")[-1]+"  "+str(i['info_image'])
    	print (yuju)
        os.system(yuju)