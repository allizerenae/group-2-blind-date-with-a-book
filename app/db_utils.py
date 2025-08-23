import mysql.connector
from database.config import USER, PASSWORD, HOST, DATABASE

class DbConnectionError(Exception):
    pass

def _connect_to_db():
    """
    Connect to MySQL database. Uses mysql_native_password for local testing.
    """
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',  # simpler local auth
        database=DATABASE,
        port=3306
        # ssl_disabled=True  # Uncomment if your server requires SSL disabled
    )
    return cnx



def view_all_books_db():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print(f"Connected to DB: {DATABASE}")
        query = """SELECT * FROM book_tracker"""
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    except Exception as e:
        print("Error reading all books:", e)
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def view_latest_book_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        port=3306,
        auth_plugin='caching_sha2_password'
    )

    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print(f"Connected to DB: {DATABASE}")
        query = """SELECT * FROM book_tracker ORDER BY book_id DESC LIMIT 1;"""
        cur.execute(query)
        result = cur.fetchone()
        cur.close()
        return result
    except Exception as e:
        print("Error reading latest book:", e)
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def add_new_book_db(new_book_dict):
    db_connection = None  # fix UnboundLocalError
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print(f"Connected to DB: {DATABASE}")

        print("ADD THIS BOOK TO DB:", new_book_dict)

        query = """ 
        INSERT INTO book_tracker (book_title, author, genre, assigned_date, deadline) 
        VALUES (%s, %s, %s, %s, %s)
        """

        title = new_book_dict["book_title"]
        author = new_book_dict["author"]
        genre = new_book_dict["genre"]
        assigned_date = new_book_dict["assigned_date"]
        deadline = new_book_dict["deadline"]

        cur.execute(query, (title, author, genre, assigned_date, deadline))
        db_connection.commit()

        print("Book added successfully!")
        return {"message": "Book added successfully!"}

    except Exception as e:
        print("Error adding book:", e)
        raise DbConnectionError("Failed to insert data into DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

if __name__ == "__main__":
    try:
        cnx = _connect_to_db()
        print("Connected successfully")
        cnx.close()
    except Exception as e:
        print("Connection failed:", e)

