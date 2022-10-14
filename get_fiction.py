import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.goodreads.com/genres/most_read/adventure")
soup = BeautifulSoup(res.text,"html.parser")
# books = soup.select(".bookImage")

book_list = []
# for book in books:
#     book_title = book.get("alt")
#     book_list.append(book_title)
    

book_image = soup.select(".coverWrapper a")
if (len(book_image)!=0):
    image_list = []
    for image in book_image:
        #book title
        book = image.select_one(".bookImage")
        book_title = book.get("alt")
        book_list.append(book_title)

        image_url = "https://www.goodreads.com/" + image.get("href")
        image_list.append(image_url)


print(image_list[0])
print(book_list[0])

    

