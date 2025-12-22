import mysql.connector

class StudentDB:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ulthoor123"
        )

        self.cursor=self.conn.cursor()
    
    #showing the databses
    def show_db(self):
        self.cursor.execute("SHOW DATABASES")
        for db in self.cursor:
            print("-",db[0])

    #checking database exist or not 
    def database_exists(self,db_name):
        self.cursor.execute("SHOW DATABASES")
        databases=[db[0] for db in self.cursor]
        return db_name in databases
    
    #create the database
    def create_db(self,db_name):
        if self.database_exists(db_name):
            print("database already exist")
        else:
            create_query=f"CREATE DATABASE {db_name}"
            self.cursor.execute(create_query)
            self.conn.commit()
            print("database created succesfully ")
        
        self.conn.database=db_name
    
    #showing the table
    def show_tables(self):
        self.cursor.execute("SHOW TABLES")
        for table in self.cursor.fetchall():
            print("-",table[0])

    #creating table into the databse
    def create_table(self,Table_name):
        create_Tquery=f""" CREATE TABLE IF NOT EXISTS {Table_name}(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        course VARCHAR(50)
        )
        """
        self.cursor.execute(create_Tquery)
        self.conn.commit()
        print(f"table '{Table_name}' created succesfully\n")

    #insering values into the table
    def insert_student(self,Table_name,name,age,course):
        insert_query=f"INSERT INTO {Table_name} (name,age,course) VALUES (%s,%s,%s)"
        self.cursor.execute(insert_query,(name,age,course))
        self.conn.commit()
        print(f"inserted {name} into table succesfully") 
    
    #read the data 
    def get_all_student(self,Table_name):
        read_query=f"SELECT * FROM {Table_name}"
        self.cursor.execute(read_query)
        return self.cursor.fetchall()
    
    #close the connection 
    def close(self):
        self.cursor.close()
        self.conn.close()
          
db=StudentDB()
print("\nshow all databases\n")
db.show_db()
db_name=input("\nEnter your database name: ")
print()
db.create_db(db_name)

print("available table name\n")
db.show_tables()

Table_name=input("\nenter the table name:")
db.create_table(Table_name)


# db.insert_student(Table_name,"chaya",21,"AI/ml")
# db.insert_student(Table_name,"kirti",21,"ECE")

print("\ninformation about student data\n")
students=db.get_all_student(Table_name)
for i in students:
    print(i)

db.close()

