import requests
import json
import math

def tmdbdata(searchquery, searchtype, Page):
    if searchtype == "Movie":
        return movies(searchquery, Page)
    elif searchtype == "TV":
        return tvshows(searchquery, Page)
    else:
        return jsonPerson(searchquery, Page)


def jsonMovie(Name, Page):
    params = {"api_key": "0d3ee9a2b929a754d750acc53410454b", "query": Name, "page": Page}
    t = requests.get("https://api.themoviedb.org/3/search/movie", params)
    return t.json()


# def allMovies(Name, Page):
#     movies = []
#     json_dict = jsonMovie(Name, Page)
#     if json_dict["total_results"] > 0:
#         for i in range(json_dict["total_pages"]):
#             movies += jsonMovie(Name, str(i + 1))['results']
#     return movies


def movies(Name, Page):
    temp = jsonMovie(Name, Page)
    newList = []
    if temp["total_results"] > 0:
        for i in temp["results"]:
            newList.append(dict([("name", i["original_title"]),

                                 ("description", i["overview"]),

                                 ("rating", i["popularity"]),

                                 ("poster", "https://image.tmdb.org/t/p/original" + str(i["poster_path"]))]))

    return newList, temp["total_pages"]


# Search Shows

def jsonShow(Name, Page):
    params = {"api_key": "0d3ee9a2b929a754d750acc53410454b", "query": Name, "page": Page}
    t = requests.get("https://api.themoviedb.org/3/search/tv", params)
    return t.json()


# def allShows(Name):
#     shows = []
#     json_dict = jsonShow(Name, None)
#     if json_dict["total_results"] > 0:
#         for i in range(json_dict["total_pages"]):
#             shows += jsonShow(Name, str(i + 1))['results']
#     return shows


def tvshows(Name, Page):
    temp = jsonShow(Name, Page)
    newList = []
    if temp["total_results"] > 0:
        for i in temp["results"]:
            print(i)
            newList.append(dict([("name", i["original_name"]),

                                 ("description", i["overview"]),

                                 ("rating", i["popularity"]),

                                 ("poster", "https://image.tmdb.org/t/p/original" + str(i["poster_path"]))]))
            
    return newList, temp["total_pages"]


# Search by person


def jsonPerson(Name, Page):
    params = {"api_key": "0d3ee9a2b929a754d750acc53410454b", "query": Name, "page": Page}
    t = requests.get("https://api.themoviedb.org/3/search/person", params)
    return t.json()

