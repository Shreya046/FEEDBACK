import sqlite3

connection=sqlite3.connect("student.db")
cursor=connection.cursor()

cmd ="""
    CREATE TABLE IF NOT EXISTS STUDENT(
        FULLNAME TEXT NOT NULL,
        USN VARCHAR(10) PRIMARY KEY ,
        BRANCH VARCHAR(10) NOT NULL,
        SEM INTEGER NOT NULL,
        CGPA INTEGER NOT NULL 
    )
"""

cursor.execute(cmd)
connection.commit()

cmd="insert into STUDENT(FULLNAME,USN,BRANCH,SEM,CGPA) values (?,?,?,?,?)" 


cursor.execute(cmd,('Suma','4mw23ad043','AI&DS','5','8'))

connection.commit()


f=cursor.execute("select * from STUDENT").fetchall()
print(f)

r=cursor.execute("select * from STUDENT where FULLNAME=? & USN=? ",('Shreya','4mw23ad046',)).fetchall()
print(r)
connection.close()
