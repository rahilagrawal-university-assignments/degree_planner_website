from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager,login_user, current_user, login_required, logout_user
from login import loginUser
import sqlite3
from server import app
from sqlite3 import Error
import imdb
from dbFunctions import *
import datetime

currentMovie = None
currentId = 0

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pass

    return render_template("index.html")

