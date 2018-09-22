from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbMake import Courses, Prereqs

engine = create_engine('sqlite:///movies.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

def searchQuery(searchText):
    searchText = "%" + searchText + "%"
    return session.query(Movie).filter(Movie.name.ilike(searchText)).all()

def addCourse(course_code, offerings):
    try:
        newCourse = Course(course_code=course_code, offerings=offerings)
        session.add(newCourse)
        session.commit()
        return True
    except:
        return False

def addPrereq(course_code, prereq_code, faculty, school, stage):
    try:
        newPrereq = Course(course_code=course_code, prereq_code=prereq_code, faculty=faculty, school=school, stage=stage)
        session.add(newPrereq)
        session.commit()
        return True
    except:
        return False

def searchCourse(course_code):
    if course_code == None:
        return session.query(Courses).all()
    return session.query(Courses).filter_by(course_code=course_code).all()

def getPrereqs(course_code):
    return session.query(Prereqs).filter_by(course_code=course_code).all()

def searchByFacultySchool(faculty, school, stage):
    return session.query(Courses).filter_by(faculty=faculty, school=school, stage=stage)
