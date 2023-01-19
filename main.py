
#======standard func============
import json

#======custom func============
from link import get_db_data
from get_most_read import get_links
from get_genre import genre_list
from get_books import get_book_info


genres = genre_list()
all_book_data = []
for genre in genres[:10]:
    print("genre:",genre)
    most_read_books = get_links("https://www.goodreads.com/genres/most_read/"+genre)
    for book_url in most_read_books:
        print("book_url:",book_url)
        book_information = get_book_info(book_url)
        all_book_data.append(book_information)

file  = open("all_books.txt","w")
for i in all_book_data:
    file.write(str(i)+"\n")
file.close()


# with open("config.json") as json_file:
#     config = json.load(json_file)

# sql_query = """
#         SELECT *
#         FROM books
#         """

# print(get_db_data(config,sql_query))