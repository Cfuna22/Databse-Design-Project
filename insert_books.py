# Reconnect to the database
conn = mysql.connector.connect(
    host="localhost",
    database="bookstoredb",
    user="root",
    password="Agwanda@123"
)
cursor = conn.cursor()

# Sample Languages
cursor.executemany("""
INSERT INTO book_language (language_name) VALUES (%s)
""", [
    ("English",),
    ("French",),
    ("German",)
])

# Sample Countries
cursor.executemany("""
INSERT INTO country (country_name) VALUES (%s)
""", [
    ("USA",),
    ("UK",),
    ("Germany",)
])

# Sample Publishers
cursor.executemany("""
INSERT INTO publisher (name, country_id) VALUES (%s, %s)
""", [
    ("Penguin Books", 1),
    ("HarperCollins", 2),
    ("Springer", 3)
])

# Sample Authors
cursor.executemany("""
INSERT INTO author (first_name, last_name) VALUES (%s, %s)
""", [
    ("George", "Orwell"),
    ("Jane", "Austen"),
    ("Mark", "Twain")
])

# Sample Books
cursor.executemany("""
INSERT INTO book (title, isbn, language_id, publisher_id, price, quantity_in_stock)
VALUES (%s, %s, %s, %s, %s, %s)
""", [
    ("1984", "9780451524935", 1, 1, 9.99, 100),
    ("Pride and Prejudice", "9780141439518", 1, 2, 12.49, 75),
    ("Adventures of Huckleberry Finn", "9780142437179", 1, 3, 11.00, 50)
])

# Link Books and Authors
cursor.executemany("""
INSERT INTO book_author (book_id, author_id) VALUES (%s, %s)
""", [
    (1, 1),
    (2, 2),
    (3, 3)
])

# Commit and close
conn.commit()
print("Sample data inserted successfully.")
cursor.close()
conn.close()
