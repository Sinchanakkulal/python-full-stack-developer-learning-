import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ulthoor123",
    database="student_db"
)
cursor=conn.cursor()

#Create the table using the python
create_table_query="""
    CREATE TABLE IF NOT EXISTS STUDENT(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        course VARCHAR(50)
    )
"""
cursor.execute(create_table_query)
conn.commit()
print("table creted")

#insert the values into the table student 
insert_query="""
    INSERT INTO student(name,age,course) VALUES (%s,%s,%s)
"""
students_values=[
    ('priya',20,'java'),
    ('sinchana',21,'python'),
    ('sameeksha',22,'c#')
]

cursor.executemany(insert_query,students_values)
conn.commit()
print("inserted values into the student table of student_db")

#READ THE DATA from the table 
select_query="""SELECT * FROM student"""
cursor.execute(select_query)
rows=cursor.fetchall()
for i in rows:
    print(i)
conn.commit()
print("showing the table")

#delecte the data 
delete_query="""DELETE FROM STUDENT WHERE id IN(%s,%s)"""
cursor.execute(delete_query,(7,8))
conn.commit()

#update the data in the table
update_query="""
    UPDATE student SET course="java" WHERE id="2"
"""
cursor.execute(update_query)
conn.commit()
print("update the id=2 from python to java course stream")


#READ THE DATA from the table 
select_query="""SELECT * FROM student"""
cursor.execute(select_query)
rows=cursor.fetchall()
for i in rows:
    print(i)
conn.commit()
print("showing the table")

#closed the connection with the cursor and databases
cursor.close()
conn.close()