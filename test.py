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
