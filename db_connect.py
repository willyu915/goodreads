from mysql.connector.constants import ClientFlag
import mysql
try:
    sql_config = {}

    cnxn = mysql.connector.connect(**sql_config)
    if cnxn.is_connected():
        cursor = cnxn.cursor()
        print("connection success")
except Exception as e:
    print("資料庫連接失敗：", e)
finally:
    if (cnxn.is_connected()):
        cursor.close()
        cnxn.close()
        print("資料庫連線已關閉")
