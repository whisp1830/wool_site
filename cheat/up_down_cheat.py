import torndb
import random

mysql_conn = torndb.Connection("10.245.146.207:3306","wool",user="campuswool",password="campuswool",charset="utf8")

info_ids = mysql_conn.query("SELECT info_id from infos_comment")

counter = 0.0

for info_id in info_ids:
	a,b = random.randint(1,49),random.randint(1,49)
	c,d = random.randint(1,49),random.randint(1,49)

	mysql_conn.execute("update infos_comment set up=%s,down=%s where info_id=%s",str(a*b),str(c*d),info_id['info_id'])

	counter += 1

	print "process %.2f%%"%(100*counter/len(info_ids))

