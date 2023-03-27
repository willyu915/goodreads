# average_rate
# Ratings
# reviews
# publish_date

import requests
from bs4 import BeautifulSoup

def get_book_info(book_url):

    res = requests.get(book_url)
    soup = BeautifulSoup(res.text,"html.parser")
    book_data = []

    # author
    author = soup.select_one("#bookAuthors .authorName > span")
    if author == None:
        author = "error"
    else:
        author = author.text

    # title
    book_title = soup.select_one("title").text
    if author == "error":
        author = book_title.split(' by ')[1].split(" | ")[0]
    book_name = book_title.split(' by ')[0]
    
    book_data.append(author)
    book_data.append(book_name)

    # img
    img = soup.select_one("#coverImage")
    if img==None:
        img = soup.select_one(".ResponsiveImage")
    img_url = img.get("src")
    book_data.append(img_url)

    # average_rate
    average_rate = soup.select_one(".RatingStatistics__rating")
    book_data.append(average_rate.text)

    # Ratings & Reviews
    ratings = soup.select_one(".RatingStatistics__meta")
    numbers = ratings.get("aria-label")
    ratings_amount = numbers.split()[0].replace(",", "")
    reviews_amount = numbers.split()[3].replace(",", "")
    book_data.append(ratings_amount)
    book_data.append(reviews_amount)
    
    #publish date
    publish_date = soup.select_one(".FeaturedDetails > p:nth-child(2)")
    publish_date_list = publish_date.text.split()[2:]
    publish_date_number = "".join(publish_date_list).replace(",", "")
    book_data.append(publish_date_number)
    return book_data


print(get_book_info("https://www.goodreads.com/book/show/830502.It?ref=nav_sb_ss_1_15"))