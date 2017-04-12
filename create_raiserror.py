import sys
import pyodbc 
import os
import time

os.system('cls')
param = (
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=192.168.0.205,10012;'
    r'DATABASE=master;'
    r'UID=sa;'
    r'PWD=1qaz@WSX3edc'
        )

db_connection = pyodbc.connect(param)
db_connection.autocommit = True
db_cursor = db_connection.cursor()
i=10
while i < 25:
    try:
        sql_command =   ("RAISERROR ('test severity "+str(i)+"',"+str(i)+ ", 1) with log;")
        db_cursor.execute(sql_command)
        i = i + 1
        print ('try '+str(i))
    except:
        i = i + 1
        print ('exception'+str(i))
    time.sleep(1)
#db_connection.autocommit = False
db_cursor.close()
del db_cursor
db_connection.close()