import mysql.connector
import pandas as pd
import csv
import psycopg2 


#df = pd.read_csv("/workspace/Code-challenge/cru-ts-2-10.1991-2000-cutdown.txt")
#df.T.to_csv('result.csv', header=False, index=False)
file_loc = "/workspace/Code-challenge/cru-ts-2-10.1991-2000-cutdown.txt"
list = ['marker']
read_df = pd.read_csv(file_loc, header=None, names=range(60)) #read in the csv file. names tells python how many columns to expect
groups = read_df[0].isin(list).cumsum() #store the recurrence of 'marker'
tables = {'process'+str(k): g.iloc[0:] for k,g in read_df.groupby(groups)} #make a dictionary of dataframes

print(tables)

mydb = mysql.connector.connect(
   host="127.0.0.1",
   port="3306",
   user="root",
   password="Giovanni",
   db="mydatabase",
   auth_plugin="mysql_native_password"
)
mycursor = mydb.cursor()
cursor.execute("CREATE DATABASE pysql")

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


#mycursor.execute("CREATE TABLE precipitations (xref INTEGER(255), yref INTEGER(255), date VARCHAR(255), val INTEGER(255))")
#sqlTable = "INSERT INTO precipitations (xref, yref, date, val) VALUE (%s, %s, %s, %s)"
#report = [('1','148','1/1/1991','3020'),
       #('1', '148','2/1/1991','2820')]


#mycursor.executemany(sqlTable, report)
#mydb.commit()
