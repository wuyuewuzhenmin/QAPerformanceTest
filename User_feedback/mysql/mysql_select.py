#coding:utf-8

import MySQLdb



#打开数据库连接

db = MySQLdb.connect("10.9.128.47", "root", "qatest", "qa", charset='utf8')
cursor = db.cursor()
search = '闪退'
search1 = '%闪退%'
sss = '%'+search+'%'
print search,type(search)

sql = "select * from qa.users_feedback  where describ like '%s'"%sss
# sql = "select * from qa.users_feedback  where describ like ('%'+'闪退'+'%')"
# sql = "select * from qa.users_feedback  where describ like'%闪退%'"

# # db = MySQLdb.connect("10.9.196.184", "blued", "ELS5Pt4Hdx3SfGRU", "blued", charset='utf8')
# #使用cursor()方法获取操作游标
# cursor = db.cursor()
# search = '闪退'
# print search,type(search)
# #SQL 查询语句
# # sql = "select * from blued.users_feedback  where contents like '%大家啪嗒复测卡了%'"
# sql = "select * from blued.users_feedback  where contents like '%s'"%search
#执行SQL语句
ss =cursor.execute(sql)
#获取所有记录列表
print ss
results = cursor.fetchall()
print results,type(results)

try:
    if results == ():
        print "No matching data was found."
    else:
        for row in results:
            id = row[0]
            uid = row[1]
            contents = row[2]
            app = row[4]
            version = row[8]
            # print "id=%d,uid=%d,contents=%s,app=%d,version=%s" % (id, uid, contents, app, version)
            print id ,uid
except:
    print '异常了'
    #关闭数据库连接
db.close()



# def mysql():
#
#     #打开数据库连接
#     db = MySQLdb.connect("10.9.196.184", "blued", "ELS5Pt4Hdx3SfGRU", "blued", charset='utf8')
#     #使用cursor()方法获取操作游标
#     cursor = db.cursor()
#     #SQL 查询语句
#     sql = "select * from blued.users_feedback  where contents like '%大家啪嗒复测卡了%'"
#     #执行SQL语句
#     ss =cursor.execute(sql)
#     #获取所有记录列表
#     print ss
#     results = cursor.fetchall()
#
#     try:
#         if results == ():
#             print "No matching data was found."
#         else:
#             for row in results:
#                 id = row[0]
#                 uid = row[1]
#                 contents = row[2]
#                 app = row[4]
#                 version = row[8]
#                 # print "id=%d,uid=%d,contents=%s,app=%d,version=%s" % (id, uid, contents, app, version)
#                 print id ,uid
#     except:
#         print '异常了'
#     #关闭数据库连接
#     db.close()
#
# if __name__ == '__main__':
#     mysql()

