# First do $ pip install mysql-connector-python --user 
import mysql.connector

mydb = mysql.connector.connect(
  host="HOSTNAME",
  user="USER",
  passwd="PASSWORD",
  database="DATABASE"
)

mycursor = mydb.cursor()

# Drop table if it exists
mycursor.execute("DROP TABLE IF EXISTS `users`;")

mycursor.execute("CREATE TABLE users (firstname VARCHAR(255), lastname VARCHAR(255), age VARCHAR(255), weight VARCHAR(255))")

for _ in range(200):
  sql = 'INSERT INTO users (firstname, lastname, age, weight) values (%s, %s, %s, %s);'
  mycursor.execute(sql, ('Test', 'User', '22', '180'))
  mydb.commit()
mydb.close()