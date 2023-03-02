import requests
from bs4 import BeautifulSoup as BS

url = "https://kg-portal.ru/movies/s_year/2021/"
requests = requests.get(url)

soup = BS(requests.text, "html.parser")

films = soup.find_all("div", class_="title")
for film in films:
    film = film.find("a")
    if film != None:
        print(film.text)