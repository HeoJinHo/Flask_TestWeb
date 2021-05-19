from flask import Flask, render_template, request, redirect, session
from flask_paginate import Pagination, get_page_args
import DBConnect

app = Flask(__name__)

# DB EX)
# db = DBConnect.connection.get_database("TestDb")
# coll = db.get_collection("CompanyInfo")
# coll.insert_many(question_list)

users = list(range(100))


def get_users(offset=0, per_page=10):
    return users[offset: offset + per_page]


@app.route('/')
def hello_world():

    print(session.get("p_id"))

    if session.get("p_id") == None:
        return redirect("/login")

    db = DBConnect.connection.get_database("TestDb")
    coll = db.get_collection("CompanyInfo")

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    # total = len(users)
    total = round(coll.find().count())

    # print("perpage")
    # print(offset, per_page, page, total, users)
    # print("pe")

    arr = []

    list = coll.find().skip((page - 1) * 10).limit(10)

    for i in list:
        arr.append(i)

    print(arr)

    pagination_user = get_users(offset=offset, per_page=per_page)

    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    return render_template('index.html',
                           users=arr,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route("/login")
def login():
    return render_template("login.html")

app.secret_key = "ABCDEFG"

@app.route("/login_check", methods=['GET', 'POST'])
def login_check():
    if request.method == 'POST':
        db = DBConnect.connection.get_database("TestDb")
        coll = db.get_collection("Users")
        id = request.form["p_id"]
        pwd = request.form["p_pwd"]

        cnt = coll.find({"id": id, "pwd":pwd}).count()

    if cnt > 0:
        print(request.form["p_id"])
        session['p_id'] = request.form["p_id"]
        session['p_pwd'] = request.form["p_pwd"]
        return redirect("/")
    check_msg = "아이디 또는 비밀번호를 확인해주세요."

    return render_template("login.html", check=check_msg)


if __name__ == '__main__':
    app.run(debug=True)
