import re
from flask import Flask,request,make_response,jsonify
from flask_cors import CORS
from cipher import hash,auth_string
from datetime import timedelta
from mail_send import authmail
import config
from db.models import User,Thread,Group,Comment
from db.database import db,init_db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')
init_db(app)
CORS(app)

## メール送信
@app.route('/send', methods=['POST'])
def email_send():
    if request.method == 'POST':
        data = request.get_json()
        code = auth_string()
        if re.match(r".*@kagawa-u\.ac\.jp",data["email"]):
            authmail(mailadress=data["email"],number=code)
            return make_response(jsonify({"state":True,"auth_code":code}))
        else:
            return make_response(jsonify({"state":False}))

## ユーザ登録
@app.route('/signup', methods=['POST'])
def user_registe():
  if request.method == 'POST':
    user = request.get_json()
    group_list = []
    if re.match(r"s[0-9]{2}t[0-9]{3}",user["email"].split("@")[0]):
        pass
    user_info = User(
      user_name = user['name'],
      email = user['email'],
      groups = ",".join(user["group"]),
      password = hash(user['password'])
    )
    db.session.add(User(user_info))
    db.session.commit()
    return make_response(jsonify({"state":True}))

## ログイン認証
@app.route("/login",methods=["POST"])
def login():
    user = request.get_json()
    user_info = db.session.query(User).filter(User.name == user["name"],
                                User.password == hash(user["password"]))
    if user_info == None:
        return False
    else:
        return user_info

## ユーザ探索
@app.route("/usersearch",methods=["GET","POST"])
def profile_get():
    user_id = request.get_json()["id"]
    user_data = db.get_or_404(User,user_id)
    user_blog = db.session.query(Thread).filter(Thread.user_id == user_id)
    return make_response(jsonify({"user_info":user_data,"blog_info":user_blog}))

## グループ追加
@app.route("/groupadd",methods=["GET","POST"])
def group_add():
    user_data = request.get_json()
    user_info = db.get_or_404(User,user_data["id"])
    user_info.group = ",".join(user_data["group"])
    db.session.add(Group(user_info))
    db.session.commit()

## 記事作成
@app.route("/blogcreate",methods=["GET","POST"])
def blog_create():
    blog_info = request.get_json()
    group_id_list = [db.session.query(Group).filter(Group.name == name)["group_id"] for name in blog_info["group"]]
    blog_info["group"] = ",".join(group_id_list)
    blog_info["sub_tag"] = ",".join(blog_info["sub_tag"])
    db.session.add(Thread(blog_info))
    db.session.commit()
    thread_id = db.session.query(Thread).filter(
        Thread.title == blog_info["title"],Thread.user_id == blog_info["user_id"])["group_id"]
    comment_data = {"thread_id":thread_id,"user_id":blog_info["user_id"],"content":blog_info["commnet"]}
    db.session.add(Comment(comment_data))
    db.session.commit()

## コメント作成
@app.route("/commentcreate",methods=["POST"])
def comment_create():
    comment_data = request.get_json()
    db.session.add(Comment(comment_data))
    db.session.commit()


## 記事更新
@app.route("/blogedit",methods=["POST"])
def blog_edit():
    blog_data = request.get_json()
    blog_info = db.session.query(Thread).filter(Thread.id == blog_data["id"])
    blog_info.title = blog_data["title"]
    blog_info.group = blog_data["group"]
    blog_info.tag = blog_data["tag"]
    blog_info.open_op = blog_data["option"]
    db.session.commit()

## コメント更新
@app.route("/commentedit",methods=["POST"])
def comment_edit():
    blog_data = request.get_json()
    blog_info = db.session.query(Comment).filter(Comment.thread_id == blog_data["id"]
                                                 ,Comment.id == int(blog_info["number"]))
    blog_info.content = blog_data["content"]
    db.session.commit()

# @app.route("/blog_delate",methods=["GET","POST"])
# def delate():
#     blog_title = request.get_json()
#     blog_list = json.load(open(BLOG_PATH, 'r'))
#     for blog in blog_list:
#         if blog_list["title"]==blog_title:
#             blog_list.remove(blog)
#             break

## スレッドリスト取得
@app.route("/display",methods=["GET","POST"])
def display():
    blog_list = []
    user_group = request.get_json()["groups"]
    blog_data = db.session.query(Thread).order_by(Thread.create_date).all()
    for blog in blog_data:
        if blog.group_op and set(user_group) & set(blog.group.split(",")) == set(blog.group.split(",")):
            blog_list.append(blog)
        elif not blog.group_op and set(user_group) & set(blog.group.split(",")) != set():
            blog_list.append(blog)
    return make_response(jsonify({"blog_list":blog_list}))

## スレッド内容取得
@app.route("/contents",methods=["POST"])
def contents_get():
    blog_id = request.get_json()["id"]
    # print(blog_id)
    thread = db.session.query(Thread).filter(Thread.id == blog_id)
    comment = db.session.query(Comment).filter(Comment.thread_id == blog_id).order_by(Comment.id).all()
    return make_response(jsonify({"thread":thread,"comment":comment}))
    
if __name__ == "__main__":
    app.run(debug=True)
