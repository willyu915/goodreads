import requests
from bs4 import BeautifulSoup


def genre_list():
    page = 1
    genres = []

    while page<15:
        url = "https://www.goodreads.com/genres/list"
        url = url+"?page="+str(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text,"html.parser")
        all_genres_tags = soup.select(".mediumText.actionLinkLite")
        for i in all_genres_tags:
            genres.append(i.text)
        page = page+1
    return genres

if __name__ == "__main__":
    print(genre_list())