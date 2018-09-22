from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbFunctions import *
from showtimeAPI import *
from imdb import IMDb
import random

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movie"
    imdb_id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String(100), nullable=False)
    poster = Column(String(250), nullable=True)
    genres = Column(String(250), nullable=False)
    is_showing = Column(Boolean, default=True)

class Cinema(Base):
    __tablename__ = "cinema"
    cinema_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

class Time(Base):
    __tablename__ = "time"
    time_id = Column(Integer, primary_key=True)
    showtime = Column(String(100), nullable=False)
    cinema_id = Column(Integer, ForeignKey("cinema.cinema_id"), nullable=False)
    imdb_id = Column(Integer, ForeignKey("movie.imdb_id"), nullable=False)

class User(Base):
    __tablename__ = "users"
    username = Column(String(100), primary_key=True, autoincrement=False)
    password = Column(String(100), nullable=False)
    firstName = Column(String(100), nullable=False)
    lastName = Column(String(100), nullable=False)

def addMovie(session, id, name, poster, is_showing, genres):
    new_movie = Movie(imdb_id=id, name=name, poster=poster, is_showing=is_showing, genres=genres)
    session.add(new_movie)
    session.commit()

def addCinema(session, name):
    new_cinema = Cinema(name=name)
    session.add(new_cinema)
    session.commit()

def addTime(session, imdb_id, cinema_id, show_time):
    new_time = Time(imdb_id=imdb_id, cinema_id=cinema_id, showtime=show_time)
    session.add(new_time)
    session.commit()

def addUser(session, username, password):
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()

# this will add all the theaters supplied using the parameteres into the session 
# def addall_theaters(session ,listof_theaters):
#     for i in range(0, len(listof_theaters["cinemas"])):
#          # print("%s " % (listof_theaters["cinemas"][i]["name"]) , (listof_theaters["cinemas"][i]["id"]))
#          addCinema(session , listof_theaters["cinemas"][i]["name"] , (listof_theaters["cinemas"][i]["id"]))

# #this will add all the movies supplied into the session depending on if it is upcoming or not 
# def addall_movies(session , listof_movies , includes_upcoming):
#     for i in range(0, len(listof_movies["movies"])):
#         addMovie(session , 
#         int(get_imdbId(listof_movies["movies"][i]["id"])),
#         listof_movies["movies"][i]["title"] ,
#         listof_movies["movies"][i]["poster_image_thumbnail"] , includes_upcoming)

# #this will add all the showtimes and the times of the movies into the session 
# def addall_times(session , listof_times):
#     for i in range(0 , len(listof_times)["showtimes"]):
#         addTime(session , int(get_imdbId(len(listof_times["showtimes"][i]["movie_id"]))),
#             int(len(listof_times["showtimes"][i]["cinema_id"]))  , len(listof_times["showtimes"][i]["start_at"]))
# #goes through all the cinemas in the database and 
# def addall_plays(session):
#     theaters = session.query(Cinema).filter_by(id>0).all
#     for Cinema in theaters:
#        listof_movies =  get_movie(str(Cinema.cinema_id))
#        for i in range(0,len(listof_movies["movies"])):
#             addPlays(session ,int(get_imdbId(listof_movies["movies"][i]["movie_id"])) ,Cinema.cinema_id)



engine = create_engine('sqlite:///movies.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)

session = DBSession()

#################################################ADITYA DB STUFF###################################

# nowShowing = {"Deadpool 2" : [], "Avengers: Infinity War" : [], "Life of the Party" : [], "Breath" : [], "I Feel Pretty" : [], "Tully" : [],
#                 "Crooked House" : [], "A Quiet Place" : [], "Chappaquiddick" : [], "Rampage" : [], "Peter Rabbit" : [],
#                 "Super Troopers 2" : [], "Sherlock Gnomes" : [], "Black Panther" : [], "Blockers" : [], "Ready Player One" : [], "Truth or Dare" : [], 
#                 "Solo: A Star Wars Story" : [],  "Duck Duck Goose" : [], "The Bookshop" : [], "Cargo" : [],}
# ia = IMDb()

# for k in nowShowing.keys():
#     movie = ia.search_movie(k)[0]
#     nowShowing[k].append(ia.get_imdbID(movie))
#     print(movie["title"])

# for k,v in nowShowing.items():
#     movieInfo = getMovieInfo("tt"+v[0])
#     print("movieInfo " + k)
#     nowShowing[k].append(movieInfo["movies"][0]["poster_image"]["image_files"][3]["url"])
    
#     genreString = ""
#     for genre in movieInfo["movies"][0]["genres"]:
#         if str(genre["name"]) == "Science Fiction":
#             genreString += "Sci-Fi "
#             continue
#         genreString += str(genre["name"] + " ")
#     nowShowing[k].append(genreString)
#     print(nowShowing[k])
#     addMovie(session, v[0], k, v[1], True, v[2])

# comingSoon = {
#     "Ocean's 8" : [],
#     "Jurrasic World: Fallen Kingdom" : [],
#     "Gringo" : [],
#     "Tag" : [],
#     "Incredibles 2" : [],
#     "Skyscraper" : [],
#     "The Equalizer 2" : [], 
#     "Kodachrome" : [],
#     "Upgrade" : [],
# }

# for k in comingSoon.keys():
#     movie = ia.search_movie(k)[0]
#     comingSoon[k].append(ia.get_imdbID(movie))
#     print(movie["title"])

# for k,v in comingSoon.items():
#     movieInfo = getMovieInfo("tt"+v[0])
#     comingSoon[k].append(movieInfo["movies"][0]["poster_image"]["image_files"][1]["url"])
#     genreString = ""
#     for genre in movieInfo["movies"][0]["genres"]:
#         if str(genre["name"]) == "Science Fiction":
#             genreString += "Sci-Fi "
#             continue
#         genreString += str(genre["name"] + " ")
#     comingSoon[k].append(genreString)
#     print(comingSoon[k])
#     addMovie(session, v[0], k, v[1], False, v[2])

# events = ["Beverly Hills", "Burwood", "Castle Hill", "Cronulla", "George Street", "Hornsby", "Kotara",
#             "Liverpool", "Miranda", "Newcastle", "Shellharbour", "Tuggerah", "Bondi Junction", "Campbelltown",
#             "Coffs Harbour", "Drive in Blacktown", "Glendale", "Hurstville", "Lismore", "Macquarie", "Moonlight Cinema Sydney",
#             "Parramatta", "Top Ryde City", "Wollongong"]

# hoyts = ["Bankstown", "Blacktown", "Broadway", "Charlestown", "Chatswood Westfield", "Eastgardens", "Entertainment Quarter", 
#             "Erina", "Mt Druitt", "Penrith", "Tweed City", "Warrawong", "Warringah Mall", "Wetherill Park"]

# readingCinemas = ["Auburn", "Charlestown", "Dubbo", "Maitland", "Rhodes", "Rouse Hill"]

# for i in events:
#     addCinema(session, "Events " + i)

# for i in hoyts:
#     addCinema(session, "Hoyts " + i)

# for i in readingCinemas:
#     addCinema(session, "Reading Cinemas " + i)

# times1 = ["10.00 am", "11.00 am", "11.30 am", "12.40 pm", "1.40 pm", "2.20 pm", "3.20 pm", "5.00 pm", "6.00 pm",
#             "6.30 pm", "7.00 pm", "7.40 pm", "8.10 pm", "9.40 pm", "10.00 pm"]

# times2 = ["10.00 am", "10.40 am", "12.10 pm", "1.10 pm", "3.20 pm", "4.20 pm", "6.30 pm", "7.30 pm", "8.30 pm", "9.30 pm"]

# times3 = ["9.45 am", "11.15 am", "12.45 pm", "3.40 pm", "5.30 pm", "9.30 pm"]

# for i in range(1, len(events)+1):
#     randInt = random.randint(1,3)

#     if randInt == 1:
#         for j in times1:
#             addTime(session, nowShowing["Deadpool 2"][0], i, j)
#             addTime(session, nowShowing["Avengers: Infinity War"][0], i, j)
#     elif randInt == 2:
#         for j in times2:
#             addTime(session, nowShowing["Deadpool 2"][0], i, j)
#             addTime(session, nowShowing["Avengers: Infinity War"][0], i, j)
#     else:
#         for j in times3:
#             addTime(session, nowShowing["Deadpool 2"][0], i, j)
#             addTime(session, nowShowing["Avengers: Infinity War"][0], i, j)

#     randInt = random.randint(1,3)

#     if randInt == 1:
#         for j in times1:
#             addTime(session, nowShowing["Solo: A Star Wars Story"][0], i, j)
#             addTime(session, nowShowing["The Bookshop"][0], i, j)
#     elif randInt == 2:
#         for j in times2:
#             addTime(session, nowShowing["Solo: A Star Wars Story"][0], i, j)
#             addTime(session, nowShowing["The Bookshop"][0], i, j)
#     else:
#         for j in times3:
#             addTime(session, nowShowing["Solo: A Star Wars Story"][0], i, j)
#             addTime(session, nowShowing["The Bookshop"][0], i, j)
    
#     randInt = random.randint(1,3)

#     if randInt == 1:
#         for j in times1:
#             addTime(session, nowShowing["Tully"][0], i, j)
#             addTime(session, nowShowing["Life of the Party"][0], i, j)
#     elif randInt == 2:
#         for j in times2:
#             addTime(session, nowShowing["Tully"][0], i, j)
#             addTime(session, nowShowing["Life of the Party"][0], i, j)
#     else:
#         for j in times3:
#             addTime(session, nowShowing["Tully"][0], i, j)
#             addTime(session, nowShowing["Life of the Party"][0], i, j)

# for i in range(len(events), len(events) + len(hoyts)+1):
#     randInt = random.randint(1,3)

#     if randInt == 1:
#         for j in times1:
#             addTime(session, nowShowing["Deadpool 2"][0], i, j)
#             addTime(session, nowShowing["Avengers: Infinity War"][0], i, j)
#     elif randInt == 2:
#         for j in times2:
#             addTime(session, nowShowing["Deadpool 2"][0], i, j)
#             addTime(session, nowShowing["Avengers: Infinity War"][0], i, j)
#     else:
#         for j in times3:
#             addTime(session, nowShowing["Deadpool 2"][0], i, j)
#             addTime(session, nowShowing["Avengers: Infinity War"][0], i, j)

#     randInt = random.randint(1,3)

#     if randInt == 1:
#         for j in times1:
#             addTime(session, nowShowing["Solo: A Star Wars Story"][0], i, j)
#             addTime(session, nowShowing["The Bookshop"][0], i, j)
#     elif randInt == 2:
#         for j in times2:
#             addTime(session, nowShowing["Solo: A Star Wars Story"][0], i, j)
#             addTime(session, nowShowing["The Bookshop"][0], i, j)
#     else:
#         for j in times3:
#             addTime(session, nowShowing["Solo: A Star Wars Story"][0], i, j)
#             addTime(session, nowShowing["The Bookshop"][0], i, j)
    
#     randInt = random.randint(1,3)

#     if randInt == 1:
#         for j in times1:
#             addTime(session, nowShowing["Tully"][0], i, j)
#             addTime(session, nowShowing["Life of the Party"][0], i, j)
#     elif randInt == 2:
#         for j in times2:
#             addTime(session, nowShowing["Tully"][0], i, j)
#             addTime(session, nowShowing["Life of the Party"][0], i, j)
#     else:
#         for j in times3:
#             addTime(session, nowShowing["Tully"][0], i, j)
#             addTime(session, nowShowing["Life of the Party"][0], i, j)

# for i in range(len(events)+len(hoyts), len(events)+len(hoyts)+len(readingCinemas)+1):
#     randInt = random.randint(1,3)

#     if randInt == 1:
#         for j in times1:
#             addTime(session, nowShowing["Deadpool 2"][0], i, j)
#             addTime(session, nowShowing["Avengers: Infinity War"][0], i, j)
#     elif randInt == 2:
#         for j in times2:
#             addTime(session, nowShowing["Deadpool 2"][0], i, j)
#             addTime(session, nowShowing["Avengers: Infinity War"][0], i, j)
#     else:
#         for j in times3:
#             addTime(session, nowShowing["Deadpool 2"][0], i, j)
#             addTime(session, nowShowing["Avengers: Infinity War"][0], i, j)

#     randInt = random.randint(1,3)

#     if randInt == 1:
#         for j in times1:
#             addTime(session, nowShowing["Solo: A Star Wars Story"][0], i, j)
#             addTime(session, nowShowing["The Bookshop"][0], i, j)
#     elif randInt == 2:
#         for j in times2:
#             addTime(session, nowShowing["Solo: A Star Wars Story"][0], i, j)
#             addTime(session, nowShowing["The Bookshop"][0], i, j)
#     else:
#         for j in times3:
#             addTime(session, nowShowing["Solo: A Star Wars Story"][0], i, j)
#             addTime(session, nowShowing["The Bookshop"][0], i, j)
    
#     randInt = random.randint(1,3)

#     if randInt == 1:
#         for j in times1:
#             addTime(session, nowShowing["Tully"][0], i, j)
#             addTime(session, nowShowing["Life of the Party"][0], i, j)
#     elif randInt == 2:
#         for j in times2:
#             addTime(session, nowShowing["Tully"][0], i, j)
#             addTime(session, nowShowing["Life of the Party"][0], i, j)
#     else:
#         for j in times3:
#             addTime(session, nowShowing["Tully"][0], i, j)
#             addTime(session, nowShowing["Life of the Party"][0], i, j)

###################################################################################################

#for upcomingdates
# date = datetime.date.today() + datetime.timedelta(days=7)

# #add Cinemas
# #the arguments location , distance 
# addall_theaters(session , get_theaters("-33.939961, 151.22966" , 5))
# #add Movies 
# #arguments you can add a theater_id to make it precise
# addall_movies(session , get_movie("") , False);
# addall_movies(session , get_all_upcoming(date))
# #add showtimes
# #arguments you can use cinema id or movie id aswell to make it more specific
# addall_times(session , get_Showtimes("" , ""))
# addall_plays(session)

# engine = create_engine('sqlite:///movies.db')
# Base.metadata.create_all(engine)
# DBSession = sessionmaker(bind=engine)

# session = DBSession()

# addMovie(session, 4154756, "Avengers: Infinity War", "http://image.tmdb.org/t/p/w154/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg", True, "Action Adventure Fantasy Sci-Fi")
# addMovie(session, 2231461, "Rampage", "http://image.tmdb.org/t/p/w154/30oXQKwibh0uANGMs0Sytw3uN22.jpg", True, "Action Adventure Sci-Fi")
# addMovie(session, 6644200, "A Quiet Place", "http://image.tmdb.org/t/p/w154/mrepRTUhNKU70PFf7LNQypbkH00.jpg", True, "Drama Horror Sci-Fi Thriller")
# addMovie(session, 1677720, "Ready Player One", "http://image.tmdb.org/t/p/w154/pU1ULUq8D3iRxl1fdX2lZIzdHuI.jpg", False,  "Action Adventure Sci-Fi")
# addMovie(session, 6791096, "I Feel Pretty", "http://image.tmdb.org/t/p/w154/bZe6x2fKtwVDsAvZQ9fnIJznBrc.jpg", False, "Comedy")

# addCinema(session, "Events Parramatta")

# results = session.query(Movie).filter_by(name="Avengers: Infinity War").all()

# movie = results[0]
# # or u can use a for loop like this:
# # for row in results:
# #   do something with row eg, row.imdb_id, row.name

# results = session.query(Cinema).filter_by(name="Events Parramatta").all()

# cinema = results[0]

# addPlays(session, movie.imdb_id, cinema.cinema_id)

# addShowtime(session, "10.00 am")

# results = session.query(Showtime).filter_by(time="10.00 am").all()

# shows = results[0]

# addTime(session, movie.imdb_id, cinema.cinema_id, shows.showtime_id)

# addUser(session, "aditya", "aditya")


