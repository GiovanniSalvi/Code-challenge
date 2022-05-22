import mysql.connector
import pandas as pd
import csv
import psycopg2 
import pymysql, sqlalchemy


df = pd.read_csv("/workspace/Code-challenge/cru-ts-2-10.1991-2000-cutdown.txt")
df.T.to_csv('result.csv', header=False, index=False)

print(df)
#print(tables)

mydb = mysql.connector.connect(
   host="127.0.0.1",
   port="3306",
   user="root",
   password="Giovanni",
   db="mydatabase"
)
mycursor = mydb.cursor()
cursor.execute("CREATE DATABASE mydatabase")

#fileLines = fileLines.rstrip("\\n")
#character1 = ","
#fileString = df.replace(character1, " ")
#character2 = "  "
#fileString = df.replace(character2, " ")
#grids = fileString
#for grid in grids:
  #splitGrids = grid.split(' ')
  #count = 0
  #for splitGrid in splitGrids:
    #if (count == 0):
      #xref = splitGrid
      #count += 1
   # if (count == 1):
      #count += 1
#df.close()


mycursor.execute("CREATE TABLE precipitations (xref INTEGER(255), yref INTEGER(255), date VARCHAR(255), val INTEGER(255))")
sqlTable = "INSERT INTO precipitations (xref, yref, date, val) VALUE (%s, %s, %s, %s)"
report = [('1','148','1/1/1991','3020'),
       ('1', '148','2/1/1991','2820')]


mycursor.executemany(sqlTable, report)
mydb.commit()
