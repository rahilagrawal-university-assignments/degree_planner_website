from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbMake import Movie, Cinema, Time, User

engine = create_engine('sqlite:///movies.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

def movieQuery(name, id, is_showing):
    if name is None and is_showing is None and id is None:
        return session.query(Movie).all()
    elif name is None and is_showing is not None and id is None:
        return session.query(Movie).filter_by(is_showing=is_showing).all()
    elif name is not None and is_showing is None and id is None:
        return session.query(Movie).filter_by(name=name).all()
    elif name is None and is_showing is None and id is not None:
        return session.query(Movie).filter_by(imdb_id=id).all()
    else:
        return session.query(Movie).filter_by(name=name, is_showing=is_showing).all()

def cinemaQuery(cinema_id):
    if cinema_id is None:
        return session.query(Cinema).all()

    return session.query(Cinema).filter_by(cinema_id=cinema_id).all()

def timeQuery(imdb_id):
    if imdb_id is None:
        return session.query(Time).all()

    return session.query(Time).filter_by(imdb_id=imdb_id).all()

def checkUser(username, password):
    result = session.query(User).filter_by(username=username, password=password).all()
    if result:
        return True
    return False

def getUser(username):
    result = session.query(User).filter_by(username=username).all()
    return result

def searchQuery(searchText):
    searchText = "%" + searchText + "%"
    return session.query(Movie).filter(Movie.name.ilike(searchText)).all()

def newUser(username, password, firstName, lastName):
    try:
        new_user = User(username=username, password=password, firstName=firstName, lastName=lastName)
        session.add(new_user)
        session.commit()
        return True
    except: 
        return False
