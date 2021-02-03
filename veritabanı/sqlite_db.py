import sqlite3

connection = sqlite3.connect("chinook.db") 
# connection = sqlite3.connect("node_app.db") ## eger yoksa oluşturur
cursor = connection.cursor()
cursor.execute("select * from customers")
for x in cursor.fetchall():
    print(x)
connection.close()