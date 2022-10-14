# img_url
# book_title
# average_rate
# Ratings
# reviews
# Author
# publish_date

import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.goodreads.com/book/show/58341222-reminders-of-him")
soup = BeautifulSoup(res.text,"html.parser")
book_title = soup.select_one("#bookTitle").text


print(book_title)

# book_list = []
# for book in books:
#     book_title = book.get("alt")
#     book_list.append(book_title)