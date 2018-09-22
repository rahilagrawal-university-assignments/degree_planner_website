from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Courses(Base):
    __tablename__ = "courses"
    course_code = Column(String(10), primary_key=True, autoincrement=False)
    offerings = Column(String(250), nullable=True)
    faculty = Column(String(250), nullable=True)
    school = Column(String(250), nullable=True)
    stage = Column(String(250), nullable=True)

class Prereqs(Base):
    __tablename__ = "prereqs"
    prereq_id = Column(Integer, primary_key=True, autoincrement=True)
    course_code = Column(String(10), nullable=False)
    prereq_code = Column(String(10), nullable=False)

engine = create_engine('sqlite:///courses.db')
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


