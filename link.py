# coding=big5

import json
import mysql
import mysql.connector


with open("config.json") as json_file:
    sql_config = json.load(json_file)

query = """
        show columns from test_table;
        """

out_data = []
cnxn = mysql.connector.connect(**sql_config)
cursor = cnxn.cursor()
cursor.execute(query)
get_data = cursor.fetchall()
cursor.close()
cnxn.close()

for j in get_data:
    out_data.append(list(j))
print(out_data)