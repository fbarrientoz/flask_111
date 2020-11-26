#!/usr/bin/env python 3
# -*- coding: utf8 -*-

from flask import g
from app import app #from the app module import
import sqlite3

DATABASE = "my_page.db"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db= g._database = sqlite3.connect(DATABASE)
    return db

def return_users():
    cursor = get_db().execute("SELECT * FROM USER", ())
    results = cursor.fetchall()
    cursor.close()
    return results
    

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    return "Hello world!"

@app.route("/aboutme")
def about_me():
    me = {"first_name" : "Fabiola",
          "last_name" : "Barrientos",
          "hobbies" : "Listen to music"
        }
    return me

