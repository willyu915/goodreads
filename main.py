
#======standard func============
import json

#======custom func============
from link import get_db_data
from get_most_read import get_title_and_image
from get_genre import genre_list


with open("config.json") as json_file:
    config = json.load(json_file)

sql_query = """
        SELECT *
        FROM books
        """

print(get_db_data(config,sql_query))
print(get_title_and_image("https://www.goodreads.com/genres/most_read/comics"))