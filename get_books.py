# average_rate
# Ratings
# reviews
# publish_date

import requests
from bs4 import BeautifulSoup

def get_book_info(book_url):

    header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
              "Accept-Encoding" : "gzip, deflate, br",
              "Accept-Language" : "en-US,en;q=0.9",
              "Host" : "www.goodreads.com",
              "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
             }
    res = requests.get(book_url, headers=header)
    # return res.text
    soup = BeautifulSoup(res.text,"html.parser")
    book_data = []

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
        print("title block error",Exception)
        author = "not found"
        book_name = "no title"
    book_data.append(author)
    book_data.append(book_name)

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
        book_data.append("average_rate not found")

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


#print(get_book_info("https://www.goodreads.com/book/show/830502.It?ref=nav_sb_ss_1_15"))