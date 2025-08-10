import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE


class DbConnectionError(Exception):
    pass


def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE,
        port=3306
    )
    return cnx


def view_all_books_db():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print(f"Connected to DB: {DATABASE}")

        query = """SELECT * FROM Books"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def view_latest_book_db():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print(f"Connected to DB: {DATABASE}")

        query = """SELECT * FROM Books ORDER BY book_id DESC LIMIT 1;"""
        cur.execute(query)
        result = cur.fetchone()  # Single tuple for the Latest row

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def add_new_book_db(new_book_dict):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print(f"Connected to DB: {DATABASE}")

        print("ADD THIS BOOK TO DB:", new_book_dict)

        query = """ INSERT INTO BookHistory (book_title, author, genre, assigned_date, deadline) VALUES
                  (%s, %s, %s, %s, %s, %s) """

        title = new_book_dict["book_title"]
        author = new_book_dict["author"]
        genre = new_book_dict["genre"]
        assigned_date = new_book_dict["assigned_date"]
        deadline = new_book_dict["deadline"]

        cur.execute(query, (title, author, genre, assigned_date, deadline))

        # Commit the transaction to make the changes in the database
        db_connection.commit()

        print("Book added successfully!")


    except Exception as e:
        print("Error adding book:", e)
        raise DbConnectionError("Failed to insert data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


if __name__ == "__main__":
    print("TESTING DB CONNECTION")
