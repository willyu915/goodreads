import requests
from bs4 import BeautifulSoup


def get_title_and_image(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    book_list = []
    book_image = soup.select(".coverWrapper a")
    if (len(book_image)!=0):
        image_list = []
        for image in book_image:
            book = image.select_one(".bookImage")
            book_title = book.get("alt")
            book_list.append(book_title)

            image_url = "https://www.goodreads.com/" + image.get("href")
            image_list.append(image_url)
        return image_list, book_list
    else:
        print("error")




    

