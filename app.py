from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
import os
from create_db import create_db
from users import delete, fetch_one, get_users, add, edit, delete


def create_app(name, test= False):
    if test:
        app = Flask(name,template_folder='../../templates')
    else:
        app = Flask(name, template_folder='templates')



    @app.route("/")
    @app.route("/index")
    def index():
        data = get_users()
        return render_template("index.html",datas=data)

    @app.route("/add_user",methods=['POST','GET'])
    def add_user():
        if request.method=='POST':
            uname=request.form['uname']
            contact=request.form['contact']
            add(uname, contact)
            flash('User Added','success')
            return redirect(url_for("index"))
        return render_template("add_user.html")

    @app.route("/edit_user/<string:uid>",methods=['POST','GET'])
    def edit_user(uid):
        if request.method=='POST':
            uname=request.form['uname']
            contact=request.form['contact']
            edit(uid, uname, contact)
            flash('User Updated','success')
            return redirect(url_for("index"))
        data = fetch_one(uid)
        return render_template("edit_user.html",datas=data)
        
    @app.route("/delete_user/<string:uid>",methods=['POST','GET'])
    def delete_user(uid):
        delete(uid)
        flash('User Deleted','warning')
        return redirect(url_for("index"))

    return app

def main( db='db_web.db', create=False):
    if create:
        create_db(db)
    os.environ['DATABASE_FILENAME'] = db
    app = create_app(__name__)
    app.secret_key='admin123'
    app.run(host='0.0.0.0', port=5000)

if __name__=='__main__':
    main()