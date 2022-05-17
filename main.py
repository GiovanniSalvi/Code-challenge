import mysql.connector

file = open('/Users/giovannisalvi/PycharmProjects/Code-challenge/source/data.txt', 'r')
fileLines = file.read()
#fileLines = fileLines.rstrip("\\n")
character1 = ","
fileString = fileLines.replace(character1, " ")
character2 = "  "
fileString = fileLines.replace(character2, " ")
grids = fileString.split("Grid-ref=  ")
for grid in grids:
  splitGrids = grid.split(' ')
  count = 0
  for splitGrid in splitGrids:
    if (count == 0):
      xref = splitGrid
      count += 1
    if (count == 1):
      yref = splitGrid
      count += 1

    print(xref)
    print(yref)
file.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Giovanni",
  database="mydatabase"
)
mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE precipitations (xref INTEGER(255), yref INTEGER(255), date VARCHAR(255), val INTEGER(255))")
#sqlTable = "INSERT INTO precipitations (xref, yref, date, val) VALUE (%s, %s, %s, %s)"
#report = [('1','148','1/1/1991','3020'),
       #('1', '148','2/1/1991','2820')]


#mycursor.executemany(sqlTable, report)
#mydb.commit()
