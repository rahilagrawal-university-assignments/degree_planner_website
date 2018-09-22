import os

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

f = open("courses.txt", "r")
for line in f:
    line = line.rstrip()
    splitLine = line.split("|")
    print(splitLine[2])
    
