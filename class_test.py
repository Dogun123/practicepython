import pymysql

conn = pymysql.connect(host='localhost',user="root",password = 'qkrtpdnd123@',db="workbench",charset="utf8")
curs = conn.cursor()

sql = "select * from topic"
curs.execute(sql)
