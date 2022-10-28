import json
import mysql
import mysql.connector

with open("config.json") as json_file:
    sql_config = json.load(json_file)

query = """
        SELECT *
        FROM books
        """

try:
    """ connect """
    cnxn = mysql.connector.connect(**sql_config)
    cursor = cnxn.cursor()
    if cnxn.is_connected():
        cursor = cnxn.cursor()
        print("connection success")

        """ execute query """
        cursor.execute(query)
        
        """ get result """
        get_data = cursor.fetchall()

except Exception as e:
    print("error:", e,"\n")

finally:
    if (cnxn.is_connected()):
        """ close connect """
        cursor.close()
        cnxn.close()
        print("close")


print(get_data)