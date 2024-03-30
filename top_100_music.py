import requests
from bs4 import BeautifulSoup

# DATE =input("Enter the date you want as YYYY-MM-DD:\n")
URL="https://www.billboard.com/charts/hot-100/2018-01-15/"

response = requests.get(url=URL)
top_songs = response.text

songs_list=BeautifulSoup(top_songs,"html.parser")
songs=songs_list.select("li ul li h3")

top_music = [item.getText().split('\t')[9] for item in songs]
print(top_music)