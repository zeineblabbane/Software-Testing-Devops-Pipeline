import re
import sqlite3 as sql

def get_users():
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    data=con.execute("select * from users").fetchall()
    
    return data

def add(uname , contact):
    con=sql.connect("db_web.db")
    con.execute("insert into users(UNAME,CONTACT) values (?,?)",(uname,contact))
    con.commit()

def edit(uid, uname , contact):
    con=sql.connect("db_web.db")
    con.execute("update users set UNAME=?,CONTACT=? where UID=?",(uname,contact,uid))
    con.commit()

def fetch_one(uid):
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    data=con.execute("select * from users where UID=?",(uid,)).fetchone()
    return data

def delete(uid):
    con=sql.connect("db_web.db")
    con.execute("delete from users where UID=?",(uid,))
    con.commit()
    