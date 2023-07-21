# coding=big5

import mysql,json
import mysql.connector

def get_db_data(sql_config,query):
    out_data = []
    cnxn = mysql.connector.connect(**sql_config)
    cursor = cnxn.cursor()
    cursor.execute(query)
    get_data = cursor.fetchall()
    cursor.close()
    cnxn.close()
    for j in get_data:
        out_data.append(list(j))
    return out_data

def insert_db_data(sql_config,query,temp_data):

    cnxn = mysql.connector.connect(**sql_config)
    cursor = cnxn.cursor()
    cursor.executemany(query, temp_data)
    cnxn.commit()
    cnxn.close()
    cursor.close()
    return "insert success"

if __name__ == "__main__":
    with open("config.json") as json_file:
        config = json.load(json_file)
    sql_query = """
            SELECT *
            FROM books
            """
    print(get_db_data(config,sql_query))