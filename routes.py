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
        facultySelected = request.form.get("Faculty")
        schoolSelected = request.form.get("School")
        stage = request.form.get("Stage")
        try:
            if request.form["send"] == "true" and schoolSelected != "None":
                return redirect(url_for("completed"))
        except:
            return render_template("index.html", faculties=faculties.keys(), facultySelected=facultySelected, schools=faculties[facultySelected])

    return render_template("index.html", faculties=faculties.keys(), facultySelected=None, schools=["None"])


@app.route('/completed', methods=["GET", "POST"])
def completed():

    return render_template("completed.html")


@app.route('/plan', methods=["GET", "POST"])
def plan():

    return render_template("plan.html")

def getFacultiesSchool():
    faculty = {}
    for filename in os.listdir(os.getcwd() + "/data/undergrad"):
        f = open(os.getcwd() + "/data/undergrad" + "/" + filename, "r")
        schools = f.readlines()
        for i in range(0 , len(schools)):
            schools[i] = schools[i].rstrip()
        faculty[filename] = schools
    return faculty

def checkPrereq(course, completed_courses):
    prereqs = getPrereqs()
    for prereq in prereqs:
        if prereq not in completed_courses:
            return False
    return True

