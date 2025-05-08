import mysql.connector
dataBase = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = 'ngoa'

)

# prepare a cursor objecct 
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")
print("all done")