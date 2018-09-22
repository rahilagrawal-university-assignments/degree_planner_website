from flask import Flask, redirect, render_template, request, url_for
import sqlite3
from server import app
from sqlite3 import Error
from dbFunctions import *
import os

@app.route('/', methods=["GET", "POST"])
def index():
    faculties = getFacultiesSchool()
    print(request.method)
    if request.method == "POST":
        facultySelected = request.form.get("Faculty")
        return render_template("index.html", faculties=faculties.keys(), facultySelected=facultySelected, schools=faculties[facultySelected])

    return render_template("index.html", faculties=faculties.keys(), facultySelected=None, schools=["None"])


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
