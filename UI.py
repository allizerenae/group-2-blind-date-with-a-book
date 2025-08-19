import requests
import json

# user interface database class - interaction with database
class UIDatabaseClass:

    #UI Database Class Attributes
    def __init__(self, base_url = "http://127.0.0.1:5000"):
        self.base_url = base_url

#option A.  Get new book and save to database
    def add_new_book_to_database_UI(self, book_data):
        endpoint1  = f"{self.base_url}/books/add"
        response = requests.post(endpoint1, headers={'content-type':'application/json'},data=json.dumps(book_data))
        return response.json()

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


# user interface class - interaction with user
class UIClass:

    # attributes
    def __init__(self, user, user_subject):
        self.user = user
        self.user_subject = ""
        self.database = UIDatabaseClass() #UIClass owns UIDatabaseClass instance

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

    #def add_new_book_to_database_UI(self, book_data):
        #Delegate the call to the database class
        #return self.database.add_new_book_to_database_UI(book_data)

if __name__ == '__main__':
    print("TESTING")


