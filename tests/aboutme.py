
from flask import g
from mypage import app

import sqlite3

DATABASE = "/home/kme05/flask_111/my_page.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_users():
    cursor = get_db().execute("select * from user", ())
    result = cursor.fetchall()
    cursor.close()
    return result

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is None:
        db.close()


@app.route('/')
# def index():
#    return 'Hello World!'
@app.route('/aboutme')
def about_me():

    me = {
        "first_name": "Jesus",
        "last_name": "Camarena",
        "hobbies": "Play Baseball :)",

    }

    return me


@app.route('/users')
def users():
    #cursor = get_db().execute("select * from user", ())
    #result = cursor.fetchall()
    #cursor.close()
    return str(get_users())

@app.route('/usersJson')
def users_json():
    out={"ok": True, "body": ""}
    users = get_users()
    body_list =[]

    for user in users:
        tmp_dic = {}
        tmp_dic["first_name"] = user[0]
        tmp_dic["last_name"] = user[1]
        tmp_dic["hoobies"] = user[2]
        body_list.append(tmp_dic)
    
    out["body"] = body_list

    return out


