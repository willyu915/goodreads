
#======standard func============
import json

#======custom func============
from link import get_db_data,insert_db_data
from get_most_read import get_links
from get_genre import genre_list
from get_books import get_book_info


genres = genre_list()
all_book_data = []
for genre in genres[70:80]:
    print("genre:",genre)
    most_read_books = get_links("https://www.goodreads.com/genres/most_read/"+genre)
    if most_read_books != None:
        for book_url in most_read_books[:5]:
            print("book_url:",book_url)
            book_information = get_book_info(book_url)
            # debug
            # with open("html_dog_man.txt","w") as file:
            #     file.write(book_information)
            # exit()
            #======
            all_book_data.append(book_information)

file  = open("all_books.txt","w")
for i in all_book_data:
    file.write(str(i)+"\n")
file.close()
exit()

with open("config.json") as json_file:
    config = json.load(json_file)

# sql_query = """
#         SELECT *
#         FROM books
#         """

# print(get_db_data(config,sql_query))

sql = "INSERT INTO books (id, title, author) VALUES (%s, %s, %s)"
val = [
  (1,'Peter', 'Lowstreet 4'),
  (2,'Amy', 'Apple st 652'),
  (3,'Hannah', 'Mountain 21'),
  (4,'Michael', 'Valley 345'),
  (5,'Sandy', 'Ocean blvd 2'),
  (6,'Betty', 'Green Grass 1'),
  (7,'Richard', 'Sky st 331'),
  (8,'Susan', 'One way 98'),
  (9,'Vicky', 'Yellow Garden 2'),
  (10,'Ben', 'Park Lane 38'),
  (11,'William', 'Central st 954')
]

print(insert_db_data(config,sql,val))