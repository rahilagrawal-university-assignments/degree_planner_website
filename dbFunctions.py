from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbMake import Courses, Prereqs

engine = create_engine('sqlite:///courses.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

def searchQuery(searchText):
    searchText = "%" + searchText + "%"
    return session.query(Movie).filter(Movie.name.ilike(searchText)).all()

def addCourse(course_code, offerings, faculty, school, stage):
    try:
        newCourse = Courses(course_code=course_code, offerings=offerings, faculty=faculty, school=school, stage=stage)
        session.add(newCourse)
        session.commit()
        return True
    except:
        pass
    
    return False

def addPrereq(course_code, prereq_code):
    try:
        newPrereq = Course(course_code=course_code, prereq_code=prereq_code)
        session.add(newPrereq)
        session.commit()
        return True
    except:
        return False

def searchCourse(course_code, faculty, school):
    if course_code == None:
        return session.query(Courses).all()
    elif course_code == None and faculty != None and school != None:
        return session.query(Courses).filter_by(faculty=faculty, school=school).all() 
    return session.query(Courses).filter_by(course_code=course_code).all()

def getPrereqs(course_code):
    return session.query(Prereqs).filter_by(course_code=course_code).all()

def searchByFacultySchool(faculty, school, stage):
    return session.query(Courses).filter_by(faculty=faculty, school=school, stage=stage)



# f = open("courses.txt", "r")
# for line in f:
#     line = line.rstrip()
#     splitLine = line.split("|")
#     print(addCourse(splitLine[0], splitLine[2], "Faculty of Engineering", "School of Computer Science and Engineering", "Undergraduate"))
# f.close()
