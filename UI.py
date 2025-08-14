import requests
import json
from book_api import get_random_book_by_genre
"""
User Interface Classes
"""

# user interface class - interaction with user

class UIClass:

    # attributes
    def __init__(self, user, user_subject):
        self.user = user
        self.user_subject = ""

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

    def user_genre_choice(self, user_genre_choice):
        if user_genre_choice == "A":
            self.user_subject = "Horror"
        if user_genre_choice == "B":
            self.user_subject = "Comedy"
        if user_genre_choice == "C":
            self.user_subject = "Romance"
        if user_genre_choice == "D":
            self.user_subject = "Random"


    #Option A.  Function to get new book
    #Calls Open Library API
    #Do we need this??!!!
    def get_new_book(self):
        print ("Generating new book")
        return get_random_book_by_genre(self.user_subject)


# user interface class - interaction with database

class UIDatabaseClass:

    #UI Database Class Attributes
    def __init__(self, base_url = "http://127.0.0.1:5000"):
        self.base_url = base_url


    #Function to get new book data from book_api...
    #....and pass to db_utils.
    #data from book_api needs to turn into a dictionary for use by db_utils
    def create_new_book_dictionary_UI(self, title, author, subject):
       new_book = {
            'title': title,
            'author': author,
            'genre': subject
        }
       return new_book

    def add_new_book_to_database_UI(self, new_book_dictionary):
        endpoint1  = f"{self.base_url}/books/add"
        new_book = requests.post(endpoint1, headers={'content-type':'application/json'},data=json.dumps(new_book_dictionary))
        return new_book


#option B.  Function to view current book and deadline
    def view_current_book_UI(self):
        endpoint2 = f"{self.base_url}/books/current"
        current_book_data = requests.get(endpoint2)
        return current_book_data.json()

#Option C. Function to view all books in the database (incl. current book)
    def view_all_books_UI(self):
        endpoint3 = f"{self.base_url}/books"
        view_all_books_data = requests.get(endpoint3)
        return view_all_books_data.json()


if __name__ == '__main__':
    #print("TESTING")
    #This is just for testing.  Actual code will be in main.py
    username = input("Hello! Please tell me your name: ").strip().capitalize() #format to clear any white space and give cap letter
    if username == "":
        username = "Reader" #Optional - just call them 'reader' if they don't give a name
    main_user = UIClass(username)
    print(UIClass.welcome(main_user))
    UIClass.display_options(main_user)
