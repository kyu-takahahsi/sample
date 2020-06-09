#共通
from flask import Flask
app = Flask(__name__)
#HTMLに反映
from flask import render_template
#HTMLから抽出
from flask import request
#ランダム選択
import random
#データベース操作
import mysql.connector
from mysql.connector import errorcode

#7章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
#/がアドレスの最後につく
@app.route("/")
def index():
    return "Index Page"

/helloがアドレスの最後につく
@app.route("/hello")
def hello():
    return "Hello, World"
"""

#8章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return "User {}".format(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return "Post {}".format(post_id)

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show the subpath after /path/
    return "Subpath {}".format(subpath)
"""

#9章ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
@app.route('/hello')
def hello():
    return render_template('hello.html', name="コード太郎")

#nameのなかがnameならばHello,nameと表示され、それ以外ならばHello,worldと表示される
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#usersのなかのものを一つずつ表示する
@app.route('/users')
def show_users():
    users = ["太郎", "花子", "一浪"]
    return render_template('users.html', users=users)
"""

#10章ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
"""
GETは、検索結果を表すページなどに使います。
http://www.google.co.jp/search?q=codecamp のように、GETを使ってリクエストパラメータをURLに含めると、検索結果の一覧が出ているページをブックマーク可能
ブラウザのキャッシュ機能により、2回目以降は高速表示が可能という利点があります。
POSTはユーザ名やパスワードなど秘匿性の高い情報を送信する際を代表に、セキュリティの観点から利用します。
なおPOSTを利用したからセキュリティに問題がないわけではなく、GETよりはリスクが軽減されるだけで、セキュリティ対策は別途必要となります。
この2つの使い分けとして、GETを使う明確なメリットがある場合以外は、基本的にPOSTを利用します。

#名前を入力するフォームのためのもの
@app.route("/send")
def send():
    return render_template('send.html')

@app.route("/receive", methods=["GET"])
def receive():
    if "my_name" in request.args.keys() :
        return "ここに入力した名前を表示： {}".format(request.args["my_name"])
    else:
        return "名前が未入力です"

#GET
@app.route("/get_sample")
def get_sample():
    return render_template('get_sample.html', query=request.args["query"] )

#POST
@app.route("/post_sample", methods=["GET"])
def sample(gender=""):
    return render_template('post_sample.html', gender=gender)

@app.route("/post_sample", methods=["POST"])
def post_sample():
"""

#10章課題1
"""
#kadai1のHTMLに反映
@app.route("/kadai1")
def send_name():
    return render_template('kadai1.html')

#入力された名前、性別、チェックを送信
@app.route("/kadai1", methods=["GET"])
def kadai1_post(name="", gender="", mail=""):
    return render_template('kadai1.html', name=name, gender=gender, mail=mail)

#入力された名前、性別、チェックを受信
@app.route("/kadai1", methods=["POST"])
def post_name():
    name = request.form.get("name","")
    gender = request.form.get("gender","")
    mail = request.form.get("mail","")
    return kadai1_post(name,gender,mail)
"""


#10章課題2
"""
#kadai2_send.htmlで送信
@app.route("/kadai2_send")
def kadai2_send():
    return render_template('kadai2_send.html')

#kadai2_recieve.htmlで受信
@app.route("/kadai2_recieve", methods=["POST"])
def kadai2_receive():
    #nameが""以外ならばようこそnameさんと表示、""ならば名前が未入力ですと表示
    if request.form["name"] != "" :
        return "ようこそ" + request.form["name"] + "さん"
    else:
        return "名前が未入力です"
"""

"""
ー試行錯誤ー
@app.route("/kadai2_send")
def kadai2_send(name=""):
    name = request.form.get("name", "")
    return render_template('kadai2_send.html', name=name)

@app.route("/kadai2_recieve", methods=["POST"])
def kadai2_recieve(name):
    return kadai2_send(name)

@app.route('/form')
def form():
   return render_template('form.html')

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
   if request.method == 'POST':
      result = request.form
      return render_template("confirm.html",result = result)
"""
"""
#10章課題3

#チェックされたハンドを送信
@app.route("/kadai3", methods=["GET"])
def kadai3_post(my_hand="", your_hand="", result=""):
    return render_template('kadai3.html', my_hand=my_hand, your_hand=your_hand, result=result)

#チェックされたハンドと相手のハンドを比較して勝敗を表示
@app.route("/kadai3", methods=["POST"])
def post():
    my_hand = request.form.get("my_hand", "")
    your_hand = random.choice(("グー", "チョキ", "パー"))
    if my_hand == your_hand:
        result = "Draw"
    elif (my_hand == "グー" and your_hand == "パー") or (my_hand == "チョキ" and your_hand == "グー") or (my_hand == "パー" and your_hand == "チョキ"):
        result = "Lose"
    else:
        result = "Win"
    return kadai3_post(my_hand, your_hand, result)
"""


#12章
"""
#例
@app.route("/mysql_select")
def mysql_select():
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'git上では伏せます'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名

    goods = []
    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()
        query = 'SELECT goods_id, goods_name, price FROM goods_table'
        cursor.execute(query)

        for (id, name, price) in cursor:
            item = {"goods_id":id, "goods_name":name, "price":price}
            goods.append(item)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()
    return render_template("goods.html", goods = goods)
"""

"""
@app.route("/mysql_sample")
def mysql_sample():
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'git上では伏せます'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名

    order = ""
    if "order" in request.args.keys() :
            order = request.args.get("order")

    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()

        query = 'SELECT goods_name, price FROM goods_table ORDER BY price ' + order
        cursor.execute(query)
        goods = []
        for (name, price) in cursor:
            item = {"name": name, "price":price}
            goods.append(item)
        params = {
        "asc_check" : order == "ASC",
        "desc_check" : order == "DESC",
        "goods" : goods
        }
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return render_template("goods.html", **params)
"""

"""
@app.route("/mysql_change")
def mysql_change():
    # import部分は省略
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'git上では伏せます'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名

    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()
        query = "INSERT INTO goods_table(goods_name, price) VALUES('ボールペン', 80)"
        cursor.execute(query)
        cnx.commit() # この処理が無いと変更が反映されません！

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return "終了"
"""

#12章課題1
@app.route("/mysql_kadai")
def challenge_mysql_select():
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'git上では伏せます'    # MySQLのパスワード
    dbname   = 'mydb'    # データベース名

    params = {
    }

    order = ""
    if "order" in request.args.keys():
            order = request.args.get("order")

    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()

        query = 'SELECT emp_id, emp_name, job, age FROM emp_table　WHERE job='+ order
        cursor.execute(query)
        job = []
        for (emp_id, emp_name, job, age ) in cursor:
            item = { "emp_id": emp_id, "emp_name": emp_name, "job": job, "age": age}
            job.append(item)

        params = {
        "manager_check" : order == "manager",
        "analyst_check" : order == "analyst",
        "CTO_check" : order == "CTO",
        "clerk_check" : order == "clerk",
        "job" : job
        }

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return render_template("goods.html", **params)



