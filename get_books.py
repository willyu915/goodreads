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
book_title = main_div.select_one("[data-testid='bookTitle']") #.text.replace("      ","").replace("\n","")
# author = main_div.select_one("#bookAuthors .authorName > span").text
# img_url = main_div.select_one("#coverImage").get("src")
# print(book_title,author,img_url)

print(book_title)
#=========================================
# book title
# book_title = soup.select_one("#bookTitle").text
# book_title = book_title.replace("      ","").replace("\n","")

# author
# author = soup.select_one("#bookAuthors .authorName > span")
# if author == None:
#     author = "error"
# else:
#     author = author.text

#img
# img = soup.select_one("#coverImage")
# if img:
#     img_url = img.get("src")
# else:
#     img_url = "error"