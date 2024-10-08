import mysql.connector
from mysql.connector import Error

# Fungsi untuk menghubungkan ke database MySQL
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',  
            user='root',       
            password='',       
            database='umur'    
        )

        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Fungsi untuk menambahkan data ke tabel users di database umur
def insert_user(connection, name, age):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO users (name, age) VALUES (%s, %s)"
        cursor.execute(query, (name, age))
        connection.commit()
        cursor.close()
        return True, f"User {name} added successfully!"
    except Error as e:
        return False, f"Database Error: {e}"

# Fungsi untuk mengambil data dari tabel users
def fetch_users(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT name, age FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        cursor.close()
        return users
    except Error as e:
        print(f"Error fetching users: {e}")
        return []
