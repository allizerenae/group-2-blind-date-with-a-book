from datetime import date, timedelta
from UI import UIClass
from flask_api.py import get_random_book_by_genre
from db_utils import add_new_book_db, view_all_books_db
from book import Book

def main():
    # Welcome the user
    username = input("Hello! Please tell me your name: ").strip().capitalize()
    if username == "":
        username = "Reader"

    UI = UIClass(username, "")

    UI.welcome()
    UI.display_genres()

    # Get user's genre choice
    choice = input("Enter your choice (A-D): ").strip().upper()
    UI.user_genre_choice(choice)

    # Get a random book from API
    print("Fetching a book from the Open Library API...")
    book_data = get_random_book_by_genre(UI.user_subject)

    # Extract book details
    title = book_data.get("title", "Unknown Title")
    author = book_data.get("author", "Unknown Author")
    genre = UI.user_subject

    # Assign dates
    assigned_date = date.today()
    deadline = assigned_date + timedelta(days=7)  # example: 7-day reading deadline

    # Create Book object
    book = Book(title, author, genre, assigned_date, deadline)

    # Display to user
    print("\nHere’s your blind date book:")
    print(book)

    # Save to database
    add_new_book_db(book.to_dict())
    print("\nBook saved to your reading list.")

    # Show all books in DB
    show_all = input("\nWould you like to see all saved books? (y/n): ").strip().lower()
    if show_all == "y":
        books = view_all_books_db()
        for b in books:
            print(b)

if __name__ == "__main__":
    main()
