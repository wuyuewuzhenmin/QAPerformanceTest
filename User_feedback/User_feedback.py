#coding:utf-8
from flask import Flask
from flask import request,render_template

import MySQLdb
# from mysql.mysql_select import mysql

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def user_response():
    if request.method == "POST":
        print '这是post请求'
        search = request.form.get('search1')
        search = search.encode("utf-8")
        # print search ,type(search)
        search = '%'+search+'%'
        db = MySQLdb.connect("10.9.128.47", "root", "qatest", "qa", charset='utf8')
        #使用cursor()方法获取操作游标
        cursor = db.cursor()
        #SQL 查询语句
        # sql = "select * from qa.users_feedback  where describ like'%闪退%'"
        sql = "select * from qa.users_feedback  where describ like '%s'"%search
        ss =cursor.execute(sql)
        #获取所有记录列表
        print ss
        results = cursor.fetchall()
        print results,type(results)

        # #执行SQL语句
        # ss =cursor.execute(sql)
        # #获取所有记录列表
        # # print ss
        # results = cursor.fetchall()
        # print type(results),results
        if results == ():
            print "您输入的内容无法识别"
            results = '您输入的内容无法识别'
            # results = (results,)
            print type(results),'hahha'
            return render_template('no_response.html', results=results)
        else:
            for row in results:
                id = row[0]
                uid = row[1]
                contents = row[2]
                app = row[4]
                version = row[8]
                # aa = [id,uid,contents,app,version]
                # print "id=%d,uid=%d,contents=%s,app=%d,version=%s" % (id, uid, contents, app, version)
                print id ,uid
            return render_template('base.html',results=results)


    else:
        print '这是get请求'
        search = request.form.get('search1')
        print search
        return render_template('base.html')
    # return render_template('base.html')

@app.route('/')
def index():
    return render_template('html.html')

if __name__ == '__main__':
    app.run()
