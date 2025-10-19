import mysql.connector

def create_database():
    try:
        # الاتصال بسيرفر MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='YOUR_PASSWORD_HERE'  # ← ضع الباسورد بتاع MySQL هنا
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # إنشاء قاعدة البيانات
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed.")
        except:
            pass

if __name__ == "__main__":
    create_database()
