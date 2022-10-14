import requests
from bs4 import BeautifulSoup

url = "https://www.goodreads.com/genres/list"
page = 2
genres = []


while page<15:
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    all_genres_tags = soup.select(".mediumText.actionLinkLite")
    for i in all_genres_tags:
        genres.append(i.text)
    url = url+"?page="+str(page)
    page = page+1


print(len(genres))
