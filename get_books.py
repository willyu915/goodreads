# average_rate
# Ratings
# reviews
# publish_date
# awards => string

import json
import time
import requests
from bs4 import BeautifulSoup
from date_format import datetime_format

def get_book_info(book_url):

    header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
              "Accept-Encoding" : "gzip, deflate, br",
              "Accept-Language" : "en-US,en;q=0.9",
              "Host" : "www.goodreads.com",
              "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
             }
    res = requests.get(book_url, headers=header)
    soup = BeautifulSoup(res.text,"html.parser")
    book_data = []

    #id
    get_id = book_url.split("/")[5].split("-")[0]
    if get_id.isdigit():
        book_id = get_id
    else:
        print("w")
        book_id = '99999999'
    book_data.append(book_id)

    # author
    #author = soup.select_one("#bookAuthors .authorName > span")
    author = soup.select_one(".ContributorLink .ContributorLink__name")
    if author == None:
        author = "error"
    else:
        author = author.text

    # title
    try:
        book_title = soup.select_one("title").text
        if author == "error":
            author = book_title.split(' by ')[1].split(" | ")[0]
        book_name = book_title.split(' by ')[0]
    except Exception:
        with open("html.txt","w") as file:
            file.write(res.text)
        print("title block error",Exception)
        author = "not found"
        book_name = "no title"
    book_data.append(author)
    book_data.append(book_name)
    book_data.append(book_url)

    # img
    img = soup.select_one("#coverImage")
    if img==None:
        img = soup.select_one(".ResponsiveImage")
    if img!=None:
        img_url = img.get("src")
    else:
        img_url="image not found"
    book_data.append(img_url)

    # average_rate
    average_rate = soup.select_one(".RatingStatistics__rating")
    if average_rate!=None:
        book_data.append(average_rate.text)
    else:
        book_data.append("0")

    # Ratings & Reviews
    ratings = soup.select_one(".RatingStatistics__meta")
    if ratings == None:
        ratings_amount = "0"
        reviews_amount = "0"
    else: 
        numbers = ratings.get("aria-label")
        ratings_amount = numbers.split()[0].replace(",", "")
        reviews_amount = numbers.split()[3].replace(",", "")
    book_data.append(ratings_amount)
    book_data.append(reviews_amount)
    
    #publish date
    publish_date = soup.select_one(".FeaturedDetails > p:nth-child(2)")
    if publish_date == None:
        publish_date_number = "10000101"
    else:
        publish_date_list = publish_date.text.split()[2:]
        publish_date_number = "".join(publish_date_list).replace(",", "")
        publish_date = datetime_format(publish_date_number)
    book_data.append(publish_date)

    #awards
    awards = soup.select_one("script[type='application/ld+json']")
    if awards == None:
        awards = "no awards"
    else:
        awards = json.loads(awards.text).get("awards","no awards")
    book_data.append(awards)
    return book_data

if __name__ == "__main__":
    for i in range(10):
        data = get_book_info("https://www.goodreads.com/book/show/43708708-white-fragility")
        if data[1] != 'not found':
            print(data)
            break
        time.sleep(2)
        print("!!!")