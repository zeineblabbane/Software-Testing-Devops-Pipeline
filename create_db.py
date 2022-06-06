import sqlite3 

def create_db(database_filename):
	#connect to SQLite
	#database_filename = 'db_web.db'
	con = sqlite3.connect(database_filename)

	#Create a Connection
	cur = con.cursor()

	#Drop users table if already exsist.
	cur.execute("DROP TABLE IF EXISTS users")

	#Create users table  in db_web database
	commande1 ='''CREATE TABLE "users" (
		"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
		"UNAME"	TEXT,
		"CONTACT"	TEXT
	)'''
	commande2="INSERT INTO users (UNAME,CONTACT) VALUES ('zeineb','zeineb')"
	cur.execute(commande1)
	cur.execute(commande2)

	#commit changes
	con.commit()

	#close the connection
	con.close()