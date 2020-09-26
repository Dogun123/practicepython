import pymongo

username = ''
password = ''
ip_address = 'localhost'
connection = pymongo.MongoClient()
connection = pymongo.MongoClient('mongodb://%s' % (ip_address))
# connection = pymongo.MongoClient('mongodb://%s:%s@%s' % (username, password, ip_address))
blog_session_db = connection.blog_session_db
blog_ab = blog_session_db.blog_ab

con = connection.admin.command('ismaster')

print(con)

info = connection.server_info()
print(info)