import requests
import json
import math
import urllib.request
from PIL import Image

print("## OMDB ##\n")
searchRequest = input("Search Omdb: ")
print("")

def jsonMedia(Name, Year, Type, Plot, Page):
    params = {"apikey": "8892b8ee", "s": searchRequest, "type": Type, "plot": Plot, "y": Year, "page": Page}
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
    for i in range(math.ceil(int(json_dict['totalResults'])/10)):
        movies += jsonMedia(Name, None, "movie", "full", str(i+1))['Search']
    return movies
    

def movieList(Name):
    for j in allMovies(Name):
        print(j['Title'])


def allShows(Name):
    shows = []
    json_dict = jsonMedia(Name, None, "series", None, None)
    for i in range(math.ceil(int(json_dict['totalResults'])/10)):
        shows += jsonMedia(Name, None, "series", None, str(i+1))['Search']
    return shows
    

def showList(Name):
    for j in allShows(Name):
        print(j['Title'])

def showPoster(movieDict):
    filename, headers = urllib.request.urlretrieve(movieDict)
    #returns two values; filename of downloaded png, headers aka metadata of the file ~n
    img = Image.open(filename)
    img.show()
    #i had to manually delete them of my computer from the App Data folder ~n

#showPoster(json_dict['Search'][0]['Poster'])
    
showList(searchRequest)