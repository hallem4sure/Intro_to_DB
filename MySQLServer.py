import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # الاتصال بالسيرفر
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='YOUR_PASSWORD_HERE'  # ← ضع كلمة مرور MySQL هنا
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # إنشاء قاعدة البيانات المطلوبة
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
