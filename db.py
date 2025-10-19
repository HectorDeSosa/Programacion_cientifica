# db.py
import sqlite3
def create_table():
    db = sqlite3.connect('database.db')
    query = """
    CREATE TABLE if not exists BOOKS
    (
     ID INTEGER PRIMARY KEY AUTOINCREMENT,
     NAME TEXT NOT NULL,
     PRICE INTERGER NOT NULL,
     CREATED_AT DATETIME default current_timestamp,
     COMPLETED_AT DATATIME NOT NULL
    )
    """
    cur = db.cursor()
    cur.execute(query)
    db.close()
# db.py
def insert_book(name,  completed_at, price):
    db = sqlite3.connect('database.db')
    query = """
    INSERT INTO BOOKS(NAME, COMPLETED_AT, PRICE)
    VALUES (?,?)
    """
    cur = db.cursor()
    cur.execute(query, (name, completed_at, price))
    db.commit()
    db.close()
# db.py
def get_all_books():
    db = sqlite3.connect('database.db')
    query = 'SELECT name, completed_at, price FROM BOOKS'
    cur = db.cursor()
    items_io = cur.execute(query)
    item_lst = [i for i in items_io]
    return item_lst
def update_book(book_id, updated_name, updated_completed_date, updated_price):
    db = sqlite3.connect('database.db')
    query = "UPDATE BOOKS SET NAME=?, COMPLETED_AT=? PRICE=? WHERE ID=?"
    cur = db.cursor()
    cur.execute(query, (updated_name, updated_completed_date,
                updated_price, book_id))
    db.commit()
    db.close()
def delete_book(book_id):
    # Connect to the SQLite database
    db = sqlite3.connect('database.db')
    # Define the SQL query to delete a book with a specific ID
    query = "DELETE FROM books WHERE id = ?"
    # Execute the query with the provided book ID as a parameter
    db.execute(query, (book_id,))
    # Commit the changes to the database
    db.commit()
    # Close the database connection
    db.close()

if __name__ == "__main__":
    create_table()