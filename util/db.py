from pymongo import MongoClient
import json

import sqlite3

DB_FILE="discobandit.db" # db used for this project. delete file if you want to remove all data/login info.

SERVER_ADDR="68.183.120.187"
client=MongoClient(SERVER_ADDR,27017)


def create_tables():
    db = sqlite3.connect(DB_FILE) # Open if file exists, otherwise create
    c = db.cursor()

    c.execute("CREATE TABLE if not exists users(username TEXT PRIMARY KEY, password TEXT)")
    c.execute("CREATE TABLE if not exists quests(user TEXT, locations TEXT, time TEXT)")
    c.execute("CREATE TABLE if not exists user_info(user TEXT, completed_quests TEXT)")

    db.commit()
    db.close()


def add_user(username, password):
    ''' insert credentials for newly registered user into database '''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO users VALUES(?, ?, {})".format("'none'"), (username, password))

    db.commit() #save changes
    db.close() #close database
