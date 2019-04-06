from flask import session, Flask, render_template, request, redirect, url_for


import os
app = Flask(__name__)
app.secret_key=os.urandom(32)# 32 bits of random data as a string

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
