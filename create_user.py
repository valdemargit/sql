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
while i < 50:
    sql_command =("CREATE LOGIN userok"+str(i)+" with password = '1qaz@WSX3edc';")
    sql_command1 =("CREATE USER userokk"+str(i)+" from login userokk"+str(i)+' with default_schema = aaa;')
    db_cursor.execute(sql_command)
    db_cursor.execute(sql_command1)
    i = i + 1
db_connection.autocommit = False
db_cursor.close()
del db_cursor
db_connection.close()