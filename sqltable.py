import mysql.connector

# Connect to MySQL Server
con = mysql.connector.connect(host="localhost", user="root", password="1234")
cur = con.cursor()

# Create and select database
cur.execute("create database if not exists vimalagiri2026")
cur.execute("use vimalagiri2026")

# Recreate candidate table
cur.execute("drop table if exists candidate")
cur.execute("Create table candidate(Serial_No int, Name varchar(30), class varchar(6), Post varchar(20))")
cur.execute("alter table candidate add unique index(Serial_No)")

# Recreate votes table
cur.execute("drop table if exists votes")
cur.execute("Create table votes(Serial_No int, Name varchar(30), votes int)")
cur.execute("alter table votes add unique index(Serial_No)")

# List of new candidates (Serial_No, Name, Class, Post)
candidates = [
    # Head Boy (2 candidates)
    (1, "Lious Basil Joshy", "XII A", "Head Boy"),
    (2, "Daniel Saji", "XI A", "Head Boy"),
    
    # Head Girl (2 candidates)
    (3, "Meera P V", "XII C", "Head Girl"),
    (4, "Aida Jojo", "XI B", "Head Girl"),
    
    # Sports Boy (2 candidates)
    (5, "Noha Binil", "XII A", "Sports Boy"),
    (6, "Abhinav Krishna P", "XI A", "Sports Boy"),
    
    # Sports Girl (2 candidates)
    (7, "Abhinaya Suresh", "XII B", "Sports Girl"),
    (8, "Delna Mariya Jaison", "XI B", "Sports Girl"),
    
    # Arts Boy (2 candidates)
    (9, "Naveen T.S", "XII A", "Arts Boy"),
    (10, "Chris Ullas", "XI B", "Arts Boy"),
    
    # Arts Girl (2 candidates)
    (11, "Krishnanandha P.S", "XII B", "Arts Girl"),
    (12, "Aagna Maria Sabu", "XI B", "Arts Girl"),
    
    # Discipline Boy (2 candidates)
    (13, "Adith Anuraj", "XII A", "Discipline Boy"),
    (14, "Geevarghese Basil", "XI A", "Discipline Boy"),
    
    # Discipline Girl (2 candidates)
    (15, "Annmaria Ashly", "XII B", "Discipline Girl"),
    (16, "Dilsha Nasrin", "XI B", "Discipline Girl")
]

# Insert candidates and initialize votes
for c in candidates:
    cur.execute("insert into candidate values(%s, %s, %s, %s)", c)
    cur.execute("insert into votes values(%s, %s, 0)", (c[0], c[1]))

con.commit()
con.close()
print("Database initialized successfully with 16 candidates!")
