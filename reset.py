import mysql.connector
cnx=mysql.connector.connect(user="root", password = "1234", host = "localhost", database = "vimalagiri2026")
cursor = cnx.cursor()
cursor.execute('update votes set votes=0')
cnx.commit()
