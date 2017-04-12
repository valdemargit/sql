import sys
import pyodbc 
import os

os.system('cls')
db_connection = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=192.168.0.205,10012;'
    r'DATABASE=master;'
    r'UID=sa;'
    r'PWD=1qaz@WSX3edc'
    )

db_connection.autocommit = True
db_cursor = db_connection.cursor()
i=1
while i < 100:
    sql_command =("""CREATE DATABASE baaase"""+str(i))
    db_cursor.execute(sql_command)
    i = i + 1
db_connection.autocommit = False
db_cursor.close()
del db_cursor
db_connection.close()