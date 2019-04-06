from flask import Flask, render_template, request,session,url_for,redirect,flash

from util import db, mongo
import os, csv, time, sqlite3, json
from urllib.request import Request, urlopen

import os
app = Flask(__name__)
app.secret_key=os.urandom(32)# 32 bits of random data as a string

@app.route("/")
def home():
    db.create_tables()
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/forgot-password")
def forgot():
    return render_template("forgot-password.html")

@app.route("/charts")
def charts():
    return render_template("charts.html")

@app.route("/tables")
def tables():
    return render_template("tables.html")

@app.route("/newQuest")
def newQuest():
    return render_template("newQuest.html")


@app.route("/blank")
def blank   ():
    return render_template("blank.html")

@app.route("/viewQuests")
def viewQuests():
    return render_template("viewQuests.html")




if __name__ == "__main__":
    app.debug = True
    app.run()

data = {}
