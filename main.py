import requests.exceptions
from app.ui import UIClass, UIDatabaseClass
from app.book_api import get_random_book_by_genre
from app.book import Book
from app.deadline import get_assigned_date, get_deadline


def get_valid_choice(prompt, valid_options):
    """Ensures the user enters a valid option"""
    choice = ""
    while choice not in valid_options:
        choice = input(prompt).strip().upper()
        if choice not in valid_options:
            print(f"Invalid choice. Please enter one of: {', '.join(valid_options)}.")
    return choice


def handle_backend_error(error):
    """Handles errors when connecting to or saving to the database"""
    if isinstance(error, requests.exceptions.RequestException):
        print("ERROR: Could not connect to the backend server.")
        print("Please make sure your Flask API is running correctly at http://127.0.0.1:5000/")
        print("Ensure your config file is correctly set up.")
    else:
        print(f"ERROR: Something went wrong while saving to the database. Details: {error}")


def fetch_and_save_book(ui, ui_db):
    """Gets book details from API and saves to external database"""
    print(ui.display_genres())
    genre_choice = get_valid_choice("Enter your genre choice (A-D): ", ["A", "B", "C", "D"])
    mapping = {"A": "Horror", "B": "Comedy", "C": "Romance", "D": "Random"}
    ui.user_subject = mapping[genre_choice]

    print("Fetching a book from the Open Library API...")
    data = get_random_book_by_genre(ui.user_subject)
    book = Book(
        data.get("title", "Unknown Title"),
        data.get("author", "Unknown Author"),
        data.get("genre", ui.user_subject),
        get_assigned_date(),
        get_deadline()
    )
    print("\nHere’s your blind date book:\n", book)

    try:
        if ui_db.add_new_book_to_database_ui(book.to_dict()):
            print("Book saved to your reading list.")

    except Exception as e:
        handle_backend_error(e)


def view_books(ui_db, option):
    """Prints book details"""
    try:
        data = {
            "B": ui_db.view_current_book_ui(),
            "C": ui_db.view_all_books_ui()
        }[option]
        print("\nBooks:\n")
        if isinstance(data, list):
            for b in data:
                print(b)
        else:
            print(data)

    except Exception as e:
        handle_backend_error(e)


def run():
    username = input("Hello! Please tell me your name: ").strip().capitalize() or "Reader"
    ui = UIClass(username, "")
    ui_db = UIDatabaseClass()

    print(ui.welcome())

    actions = {
        "A": lambda: fetch_and_save_book(ui, ui_db),
        "B": lambda: view_books(ui_db, "B"),
        "C": lambda: view_books(ui_db, "C")
    }

    while True:
        print(ui.display_options())
        choice = get_valid_choice("Enter your choice (A-C): ", actions.keys())
        actions[choice]()
        if input("\nReturn to main menu? (y/n): ").strip().lower() != "y":
            print("Goodbye and happy reading!")
            break


if __name__ == "__main__":
    run()
