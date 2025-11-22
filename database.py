import sqlite3

connection=sqlite3.connect("feedback.db")
cursor=connection.cursor()

cmd ="""
    CREATE TABLE IF NOT EXISTS FEEDBACK(
        ID INTEGER PRIMARY KEY ,
        FULLNAME TEXT NOT NULL,
        USN VARCHAR(10) NOT NULL,
        CONTACT VARCHAR(10) NOT NULL,
        EMAIL TEXT NOT NULL,
        MESSAGE TEXT NOT NULL
    )
"""

cursor.execute(cmd)
connection.commit()

cmd="insert into feedback(FULLNAME,USN,CONTACT,EMAIL,MESSAGE) values (?,?,?,?,?)" 


#cursor.execute(cmd,('Shreya','4mw23ad046','9084674378','shreya.23ad046@sode-edu.in','This is a good time to learn DevOps!!!'))
connection.commit()


f=cursor.execute("select * from feedback").fetchall()
print(f)
r=cursor.execute("select * from feedback where fullname=? ",('Shreya',)).fetchall()
print(r)

connection.close()
