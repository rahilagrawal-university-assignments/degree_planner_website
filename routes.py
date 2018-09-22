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
                if (stage == "Current"):
                    return redirect(url_for("completed", facultySelected=facultySelected, schoolSelected=schoolSelected))
                else:
                    return redirect(url_for("plan", facultySelected=facultySelected, schoolSelected=schoolSelected))
        except:
            return render_template("index.html", faculties=faculties.keys(), facultySelected=facultySelected, schools=faculties[facultySelected])

    return render_template("index.html", faculties=faculties.keys(), facultySelected=None, schools=["None"])


@app.route('/completed', methods=["GET", "POST"])
def completed():
    return render_template("completed.html")


@app.route('/plan', methods=["GET", "POST"])
def plan():
    t1 = []
    t2 = []
    t3 = []
    faculty = request.args.get("facultySelected")
    school = request.args.get("schoolSelected")
    if request.method == "POST":
        pass
    courseDB = searchCourse(None, faculty, school)
    courses = {}
    for c in courseDB:
        courses[c.course_code] = list(c.offerings)
    print(courses)
    return render_template("plan.html", courses=courses, t1=t1, t2=t2, t3=t3)

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
