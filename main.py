
#======standard func============
import json

#======custom func============
from link import get_db_data


with open("config.json") as json_file:
    config = json.load(json_file)

sql_query = """
        SELECT *
        FROM books
        """

print(get_db_data(config,sql_query))