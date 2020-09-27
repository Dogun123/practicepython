import pymongo

username = ''
password = ''
ip_address = 'localhost'
connection = pymongo.MongoClient()
connection = pymongo.MongoClient('mongodb://%s' % (ip_address))
# connection = pymongo.MongoClient('mongodb://%s:%s@%s' % (username, password, ip_address))
blog_session_db = connection.blog_session_db
blog_ab = blog_session_db.blog_ab

blog_logs = blog_ab.find()
for log in blog_logs:
    print(log)