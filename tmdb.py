import requests
import json
import math

#Search Movies

def jsonMovie(Name, Page):
    params = {"api_key" : "0d3ee9a2b929a754d750acc53410454b", "query" : Name, "page" : Page}
    t = requests.get("https://api.themoviedb.org/3/search/movie", params)
    return t.json()


def allMovies(Name):
    movies = []
    json_dict = jsonMovie(Name, None)
    if json_dict["total_results"] > 0:
        for i in range(json_dict["total_pages"]):
            movies += jsonMovie(Name, str(i+1))['results']
    return movies
    
def Nathan(Name):
    temp = allMovies(Name)
    newList = []
    if temp["total_results"] > 0:
        for i in temp:
            newList.append(dict([("name", i["original_title"]),("description",i["overview"]),("rating",i["popularity"]),("poster","https://image.tmdb.org/t/p/original" + i["poster_path"])]))
    
    return newList


#Search Shows

def jsonShow(Name, Page):
    params = {"api_key" : "0d3ee9a2b929a754d750acc53410454b", "query" : Name, "page" : Page}
    t = requests.get("https://api.themoviedb.org/3/search/tv", params)
    return t.json()


def allShows(Name):
    shows = []
    json_dict = jsonShow(Name, None)
    if json_dict["total_results"] > 0:
        for i in range(json_dict["total_pages"]):
            shows += jsonShow(Name, str(i+1))['results']
    return shows
    
def Nathans(Name):
    temp = jsonShow(Name, None)
    newList = []
    if temp["total_results"] > 0:
        temp2 = allShows(Name)
        for i in temp2:
            print(i)
            newList.append(dict([("name", i["original_name"]),
                                 
                                 ("description",i["overview"]),

                                 ("rating",i["popularity"]),

                                 ("poster","https://image.tmdb.org/t/p/original" + i["poster_path"])]))
    return newList



#Search by person


def jsonPerson(Name, Page):
    params = {"api_key" : "0d3ee9a2b929a754d750acc53410454b", "query" : Name, "page" : Page}
    t = requests.get("https://api.themoviedb.org/3/search/person", params)
    return t.json()

x = jsonPerson("brad pitt", None)["results"]

for i in x:
    for k, v in i.items():
        print(k, v)