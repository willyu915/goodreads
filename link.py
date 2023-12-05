# coding=big5

import mysql
import json
import mysql.connector

# https://freedb.tech/dashboard/index.php


def get_db_data(sql_config, query):
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


def insert_db_data(sql_config, query, temp_data):

    cnxn = mysql.connector.connect(**sql_config)
    cursor = cnxn.cursor()
    cursor.executemany(query, temp_data)
    cnxn.commit()
    cnxn.close()
    cursor.close()
    return "insert success"


def create_db_table(sql_config, query):
    cnxn = mysql.connector.connect(**sql_config)
    cursor = cnxn.cursor()
    cursor.execute(query)
    cursor.close()
    cnxn.close()
    return "create success"


def delete_db_data(sql_config, query):
    cnxn = mysql.connector.connect(**sql_config)
    cursor = cnxn.cursor()
    cursor.execute(query)
    cnxn.commit()
    cursor.close()
    cnxn.close()
    return "delete success"


if __name__ == "__main__":
    with open("config.json") as json_file:
        config = json.load(json_file)
    # sql_query = """
    #             delete from mains where genre <> '18th-century'
    #             """
    # print(delete_db_data(config, sql_query))

    sql_query = """
                select count(id) from mains
                """
    print(get_db_data(config, sql_query))

"""
CREATE TABLE books (id VARCHAR(255), 
                    title VARCHAR(255),
                    author VARCHAR(255), 
                    awards VARCHAR(255), 
                    publish_date DATE, 
                    image_url VARCHAR(255), 
                    book_url VARCHAR(255))
"""
"""
CREATE TABLE mains (id VARCHAR(255), 
                    genre VARCHAR(255),
                    date DATE, 
                    average_rating FLOAT, 
                    ratings_count INT, 
                    reviews_count INT)
"""
