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

main_div = soup.select_one(".BookPageTitleSection")
if main_div==None:
    main_div = soup.select_one("#metacol")
    book_title = main_div.select_one('#bookTitle').text.replace("      ","").replace("\n","")
    print("version A")
else:
    book_title = main_div.select_one('[data-testid="bookTitle"]').text
    print("version B")
# author = main_div.select_one("#bookAuthors .authorName > span").text
# img_url = main_div.select_one("#coverImage").get("src")
# print(book_title,author,img_url)

print(book_title)
#=========================================
# book title
book_title = soup.select_one("#bookTitle").text
book_title = book_title.replace("      ","").replace("\n","")

# author
author = soup.select_one("#bookAuthors .authorName > span")
if author == None:
    author = "error"
else:
    author = author.text

#img
img = soup.select_one("#coverImage")
if img:
    img_url = img.get("src")
else:
    img_url = "error"