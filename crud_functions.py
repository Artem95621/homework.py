import sqlite3


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