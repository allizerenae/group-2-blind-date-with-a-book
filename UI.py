import requests
import json
"""
User Interface Classes
"""

# user interface class - interaction with user

class UIClass:

    # attributes
    def __init__(self, user):
        self.user = user

    # methods
    def welcome(self):
        return f'''
== == == == == == == == == == == == == == == == == == == == == == == == == == 
\U0001F4DA  Hello {self.user}, Welcome to The Blind Date with a Book Portal! \U0001F4DA
== == == == == == == == == == == == == == == == == == == == == == == == == =='''
    #unicode for book emoji is \U0001F4DA
    #unicode for calendar emoji is \U0001F4C5

    #Uses Unicode to create emojis.
    def display_options(self):
        print("Please choose from the following options: ")
        print("A: Choose a new book \U0001F4DA")
        print("B: View current book and deadline \U0001F4DA \U0001F4C5 ")
        print("C: View previous books \U0001F4DA \U0001F4DA \U0001F4DA ")

    def display_genres(self):
        print ("Please choose a genre: ")
        print ("A: Horror")
        print ("B: Comedy")
        print ("C: Romance")
        print ("D: Random genre")

    #Option A.  Function to get new book
    #Calls Open Library API
    def get_new_book (self):
        pass


# user interface class - interaction with database
class UIDatabaseClass:
    def add_to_book_tracker_UI(self):
        endpoint1 = "http://127.0.0.1:5000/books/add"

#option B.  Function to view current book and deadline
    def view_current_book_UI(self):
        endpoint2 = "http://127.0.0.1:5000/books/current"
        current_book_data = requests.get(endpoint2)
        return current_book_data.json()

#Option C. Function to view all books in the database (incl. current book)
    def view_all_books_UI(self):
        endpoint3 = "http://127.0.0.1:5000/books"
        view_all_books_data = requests.get(endpoint3)
        return view_all_books_data.json()


if __name__ == '__main__':
    username = input("Hello! Please tell me your name: ").strip().capitalize() #format to clear any white space and give cap letter
    if username == "":
        username = "Reader" #Optional - just call them 'reader' if they don't give a name
    main_user = UIClass(username)
    print(UIClass.welcome(main_user))
    UIClass.display_options(main_user)
