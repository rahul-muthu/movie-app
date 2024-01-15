import requests
import json
import math


def jsonMedia(Name, Year, Type, Plot, Page):
    params = {"apikey": "8892b8ee", "s": Name, "type": Type, "plot": Plot, "y": Year, "page": Page}
    r = requests.get("https://www.omdbapi.com/", params)
    # Request object created of page 1 of all movies with "Batman"

    return r.json()
    # json decoder used to make results into a dictionary
    # the dictionary contains:
    # Search, a list of dictionaries for each movie
    # totalResults, an int showing how many movies are there
    # Response, a boolean showing if there are results are not, I assume??

def allMovies(Name):
    movies = []
    json_dict = jsonMedia(Name, None, "movie", None, None)
    if json_dict["Response"] == 'True':
        for i in range(math.ceil(int(json_dict['totalResults'])/10)):
            movies += jsonMedia(Name, None, "movie", "full", str(i+1))['Search']
        return movies
    else:
        print(json_dict["Error"])
        return []

def movieList(Name):
    for j in allMovies(Name):
        print(j['Title'])
    
def returnMovies(Name, Type):
    movies = []

    for i in allMovies(Name):
        params2 = {"api_key" : "0d3ee9a2b929a754d750acc53410454b"}
        t = requests.get("https://api.themoviedb.org/3/movie/" + i["imdbID"], params2)
        t = t.json()

        print(i["imdbID"])
        if len(t) > 3:
            movies.append(dict([("name",i["Title"]),("Poster",i["Poster"]),("Description",t["overview"]),("Rating",t["popularity"])]))
    
    
    return movies


def allShows(Name):
    shows = []
    json_dict = jsonMedia(Name, None, "series", None, None)
    if json_dict["Response"] == True:
        for i in range(math.ceil(int(json_dict['totalResults'])/10)):
            shows += jsonMedia(Name, None, "series", None, str(i+1))['Search']
        return shows
    else:
        print(json_dict["Error"])
        return []
    

def showList(Name):
    for j in allShows(Name):
        print(j['Title'])





    



