from datetime import date, timedelta
from UI import UIClass
#from flask_api import get_random_book_by_genre
from db_utils import add_new_book_db, view_all_books_db
from book_api import get_random_genre, get_random_book_by_genre
from book import Book


def main():
    username = input("Hello! Please tell me your name: ").strip().capitalize()
    if username == "":
        username = "Reader"

    UI = UIClass(username)

    print(UI.welcome())
    UI.display_genres()

    choice = input("Enter your choice (A-D): ").strip().upper()

    # Map choice to genre
    mapping = {"A": "Horror", "B": "Comedy", "C": "Romance", "D": "Random"}
    UI.user_subject = mapping.get(choice, "Random")

    print("Fetching a book from the Open Library API...")
    book_data = get_random_book_by_genre(UI.user_subject)

    title = book_data.get("title", "Unknown Title")
    author = book_data.get("author", "Unknown Author")
    genre = UI.user_subject

    assigned_date = date.today()
    deadline = assigned_date + timedelta(days=7)

    book = Book(title, author, genre, assigned_date, deadline)

    print("\nHere’s your blind date book:")
    print(book)

    add_new_book_db(book.to_dict())
    print("\nBook saved to your reading list.")

    show_all = input("\nWould you like to see all saved books? (y/n): ").strip().lower()
    if show_all == "y":
        books = view_all_books_db()
        for b in books:
            print(b)

if __name__ == "__main__":
    main()

