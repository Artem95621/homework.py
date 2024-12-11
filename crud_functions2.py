import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

dict_foto_ = {"pic1.jpg", "pic2.jpg", "pic3.jpg", "pic4.jpg", "pic5.jpg"}

def initiate_db():
    connection = sqlite3.connect('product_base.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        );
        ''')
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users(
            userid INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
            )
            """)
    connection.commit()
    connection.close()

def get_all_products(id, title, description, price):
    connection = sqlite3.connect('product_base.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products

def is_included(username):
    check_user = cursor.execute("SELECT username FROM Users WHERE username = ?", (username,))
    if check_user.fetchone():
        return True
    return False


def add_user(username, email, age):
    cursor.execute(f"INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                    (username, email, age, 1000))

    connection.commit()