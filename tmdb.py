import requests
import json
import math

def omdbdata(searchquery, searchtype):
    if searchtype == "Movie":
        return movies(searchquery)
    elif searchtype == "TV":
        return tvshows(searchquery)
    else:
        return jsonPerson(searchquery, 1)


def jsonMovie(Name, Page):
    params = {"api_key": "0d3ee9a2b929a754d750acc53410454b", "query": Name, "page": Page}
    t = requests.get("https://api.themoviedb.org/3/search/movie", params)
    return t.json()


def allMovies(Name):
    movies = []
    json_dict = jsonMovie(Name, None)
    if json_dict["total_results"] > 0:
        for i in range(json_dict["total_pages"]):
            movies += jsonMovie(Name, str(i + 1))['results']
    return movies


def movies(Name):
    temp = jsonMovie(Name, None)
    newList = []
    if temp["total_results"] > 0:
        temp2 = allMovies(Name)
        for i in temp2:
            newList.append(dict([("name", i["original_title"]),

                                 ("description", i["overview"]),

                                 ("rating", i["popularity"]),

                                 ("poster", "https://image.tmdb.org/t/p/original" + str(i["poster_path"]))]))

    return newList


# Search Shows

def jsonShow(Name, Page):
    params = {"api_key": "0d3ee9a2b929a754d750acc53410454b", "query": Name, "page": Page}
    t = requests.get("https://api.themoviedb.org/3/search/tv", params)
    return t.json()


def allShows(Name):
    shows = []
    json_dict = jsonShow(Name, None)
    if json_dict["total_results"] > 0:
        for i in range(json_dict["total_pages"]):
            shows += jsonShow(Name, str(i + 1))['results']
    return shows


def tvshows(Name):
    temp = jsonShow(Name, None)
    newList = []
    if temp["total_results"] > 0:
        temp2 = allShows(Name)
        for i in temp2:
            print(i)
            newList.append(dict([("name", i["original_name"]),

                                 ("description", i["overview"]),

                                 ("rating", i["popularity"]),

                                 ("poster", "https://image.tmdb.org/t/p/original" + str(i["poster_path"]))]))
    return newList


# Search by person


def jsonPerson(Name, Page):
    params = {"api_key": "0d3ee9a2b929a754d750acc53410454b", "query": Name, "page": Page}
    t = requests.get("https://api.themoviedb.org/3/search/person", params)
    return t.json()

