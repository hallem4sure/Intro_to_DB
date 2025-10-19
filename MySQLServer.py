import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # الاتصال بالسيرفر
        connection = mysql.connector.connect(
            host="localhost",
            user="root",      # غيّرها لو عندك يوزر مختلف
            password=""       # لو فيه باسورد اكتبه هنا
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
