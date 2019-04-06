from flask import session, Flask, render_template, request, redirect, url_for
from util import db
import json

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
    render_template("charts.html")

@app.route("/charts")
def tables():
    render_template("tables.html")








if __name__ == "__main__":
    app.debug = True
    app.run()

data = {}
