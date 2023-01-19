import requests
from bs4 import BeautifulSoup


def get_links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    book_list = []
    book_links = soup.select(".coverWrapper a")
    link_list = []
    if (len(book_links)!=0):
        for link in book_links:
            book_link = link.get("href")
            book_link = "https://www.goodreads.com/" + book_link
            link_list.append(book_link)
        return link_list
