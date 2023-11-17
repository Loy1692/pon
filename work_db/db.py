import sqlite3

connect = sqlite3.connect("work.db/shop.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(50), 
        price INTEGER, 
        count INTEGER,
        new_product INTEGER
    )
""")

# with open('work_db\\script.sql', 'r') as f:
#     cursor.executescript(f.read())

# product2 = ["MacbookPro17", 2354, 20]

product_list = [
    ['sumsung galaxy90', 300, 100],
    ['lenovo 90', 500, 300]
]

cursor.executemany("INSERT INTO products(name, price, count, new product) VALUES (?, ?, ?)", product_list)
connect.commit()

cursor.execute("SELECT * FROM categories")

products = cursor.fetchall()
print(products)

cursor.close()
connect.close()
