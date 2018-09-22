from flask import Flask, redirect, render_template, request, url_for
import sqlite3
from server import app
from sqlite3 import Error
from dbFunctions import *
import os

@app.route('/', methods=["GET", "POST"])
def index():
    faculties = getFacultiesSchool()
    if request.method == "POST":
        

    return render_template("index.html", faculties=faculties.keys())


@app.route('/existing', methods=["GET", "POST"])
def existing():

    return render_template("existing.html")


@app.route('/current', methods=["GET", "POST"])
def current():

    return render_template("current.html")

def getFacultiesSchool():
    faculty = {}
    for filename in os.listdir(os.getcwd() + "/data/undergrad"):
        f = open(os.getcwd() + "/data/undergrad" + "/" + filename, "r")
        schools = f.readlines()
        for i in range(0 , len(schools)):
            schools[i] = schools[i].rstrip()
        faculty[filename] = schools
    return faculty
