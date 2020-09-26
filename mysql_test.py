import pymysql

db_conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='qkrtpdnd123@',
    db='my_db',
    charset='utf8')

dave_db = db_conn.cursor()

# sql = """
# CREATE TABLE user_info(
#     USER_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
#     USER_EMAIL VARCHAR(100) NOT NULL,
#     BLOG_ID CHAR(4),
#     PRIMARY KEY(USER_ID)
# );
# """
# dave_db.execute(sql)
# db_conn.commit()

# user_email = 'test@test.com'
# blog_id='A'

# sql = "INSERT INTO user_info (USER_EMAIL,BLOG_ID) VALUES ('%s','%s')" % (str(user_email),str(blog_id))
# dave_db.execute(sql)
# db_conn.commit()

sql = "SELECT * FROM user_info WHERE USER_EMAIL = '" +str('test@test.com') + "'"
dave_db.execute(sql)
results = dave_db.fetchall()
for result in results:
    print(result,type(result))

db_conn.close()