from datetime import date, timedelta
from UI import UIClass, UIDatabaseClass
from book_api import get_random_book_by_genre
from book import Book

def get_valid_choice(prompt, valid_options):
    choice = ""
    while choice not in valid_options:
        choice = input(prompt).strip().upper()
        if choice not in valid_options:
            print(f"Invalid choice. Please enter one of: {', '.join(valid_options)}.")
    return choice

def fetch_and_save_book(ui, ui_db):
    ui.display_genres()
    genre_choice = get_valid_choice("Enter your genre choice (A-D): ", ["A", "B", "C", "D"])
    mapping = {"A": "Horror", "B": "Comedy", "C": "Romance", "D": "Random"}
    ui.user_subject = mapping[genre_choice]

    print("Fetching a book from the Open Library API...")
    data = get_random_book_by_genre(ui.user_subject)
    book = Book(
        data.get("title", "Unknown Title"),
        data.get("author", "Unknown Author"),
        data.get("genre", ui.user_subject),
        date.today(),
        date.today() + timedelta(days=7)
    )
    print("\nHere’s your blind date book:\n", book)
    ui_db.add_new_book_to_database_UI (book.to_dict())
    print("Book saved to your reading list.")

def view_books(ui_db, option):
    data = {
        "B": ui_db.view_current_book_UI(),
        "C": ui_db.view_all_books_UI()
    }[option]
    print("\nBooks:\n")
    if isinstance(data, list):
        for b in data:
            print(b)
    else:
        print(data)

def main():
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
        ui.display_options()
        choice = get_valid_choice("Enter your choice (A-C): ", actions.keys())
        actions[choice]()
        if input("\nReturn to main menu? (y/n): ").strip().lower() != "y":
            print("Goodbye and happy reading!")
            break

if __name__ == "__main__":
    main()

