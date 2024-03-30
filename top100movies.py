import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
top_movies = response.text

soup = BeautifulSoup(top_movies, "html.parser")
lists = soup.find_all(name="h3",class_="title")

movies_list=[item.getText() for item in lists]

with open("movies.txt", "w",encoding="utf-8") as file:
    for move in range(len(movies_list)-1,-1,-1) :
        file.writelines(f"{movies_list[move]}\n")
