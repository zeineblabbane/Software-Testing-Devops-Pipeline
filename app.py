from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql

from users import delete, fetch_one, get_users, add, edit, delete
app=Flask(__name__)

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
    
@app.route("/delete_user/<string:uid>",methods=['GET'])
def delete_user(uid):
    delete(uid)
    flash('User Deleted','warning')
    return redirect(url_for("index"))
    
if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)