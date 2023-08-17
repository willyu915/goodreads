
#======standard func============
import json
import time
from datetime import date

#======custom func============
from link import get_db_data,insert_db_data
from get_most_read import get_link_id
from get_genre import genre_list
from get_books import get_book_info

genres = genre_list()
all_book_data = []
for genre in genres[80:83]:
    print("genre:",genre)
    most_read_books = get_link_id("https://www.goodreads.com/genres/most_read/"+genre)
    if most_read_books != None:
        for book_url,book_id in most_read_books[:3]:
            print("book_url:",book_url)
            book_information = get_book_info(book_url)
            all_book_data.append([genre]+book_information)

file  = open("all_books.txt","w")
for i in all_book_data:
    file.write(str(i)+"\n")
file.close()


with open("config.json") as json_file:
    config = json.load(json_file)

# insert data to books and mains table
today_d = str(date.today())
sql_books = "INSERT INTO books (id, title, author,awards,publish_date,image_url,book_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
sql_mains = "INSERT INTO mains (id, genre, date,average_rating,ratings_count,reviews_count) VALUES (%s, %s, %s, %s, %s, %s)"

val_books = []
val_mains = []

for idx,i in enumerate(all_book_data):
    if i[1]!='99999999' and i[2]!='not found':
        val_books.append([i[1],i[3],i[2],i[-1],i[-2],i[5],i[4]])
        val_mains.append([i[1],i[0],today_d,i[-5],i[-4],i[-3]])

print(insert_db_data(config,sql_books,val_books))
print(insert_db_data(config,sql_mains,val_mains))