import mysql.connector
from mysql.connector import Error
import os
import datetime

# ------------------------------
# MySQL connection settings
# ------------------------------
# DB_HOST = os.getenv("DB_HOST","localhost")
# DB_USER = os.getenv("DB_USER","root")
# DB_PASS = os.getenv("DB_PASS","Ulthoor123")  # replace with your MySQL root password

# ------------------------------
# Log error with timestamp
# ------------------------------
def log_error(error_msg):
    with open("error_log.txt", "a") as file:
        file.write(f"{datetime.datetime.now()} - {error_msg}\n")

# ------------------------------
# Connect to MySQL server
# ------------------------------
def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ulthoor123"
        )
        return connection
    except Error as e:
        log_error(str(e))
        print("❌ MySQL connection failed. Check your credentials or server status.")
        return None

# ------------------------------
# Check if database exists
# ------------------------------
def database_exists(db_name):
    conn = connect_mysql()
    if conn is None:
        return False
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor]
    cursor.close()
    conn.close()
    return db_name in databases

# ------------------------------
# Create a new database
# ------------------------------
def create_database(db_name):
    conn = connect_mysql()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"✅ Database `{db_name}` created successfully.")
    except Error as e:
        print(f"❌ {e}")
        log_error(str(e))
    finally:
        cursor.close()
        conn.close()

# ------------------------------
# Show all databases
# ------------------------------
def show_databases():
    conn = connect_mysql()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    print("📚 List of databases:")
    for db in cursor:
        print("-", db[0])
    cursor.close()
    conn.close()

# ------------------------------
# Main menu loop
# ------------------------------
def main():
    while True:
        print("\n=== MySQL Database Manager ===")
        print("1. Create Database")
        print("2. Show Databases")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            db_name = input("Enter a database name: ").strip()
            if not db_name:
                print("❌ Database name cannot be empty.")
                continue
            if database_exists(db_name):
                print(f"⚠️ Database `{db_name}` already exists.")
            else:
                create_database(db_name)

        elif choice == "2":
            show_databases()

        elif choice == "3":
            print("👋 Exiting the program.")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

# ------------------------------
# Run program
# ------------------------------
if __name__ == "__main__":
    main()
