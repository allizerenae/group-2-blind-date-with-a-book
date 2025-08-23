import requests
import json

# user interface database class
class UIDatabaseClass:

    # UI database class attributes
    def __init__(self, base_url = "http://127.0.0.1:5000"):
        self._base_url = base_url

    #Getter for protected instance
    def get_base_url(self):
        return self._base_url

    #Setter for protected instance
    def set_base_url (self, new_value):
        if new_value != "http://127.0.0.1:5000":
            raise ValueError("base_url cannot be changed")
        self._base_url = new_value

    # Get new book and save to database
    def add_new_book_to_database_UI(self, book_data):
        endpoint1  = f"{self.get_base_url()}/books/add"
        response = requests.post(endpoint1, headers={'content-type':'application/json'},data=json.dumps(book_data))
        return response.json()

    # Function to view current book and deadline
    def view_current_book_UI(self):
        endpoint2 = f"{self.get_base_url()}/books/current"
        current_book_data = requests.get(endpoint2)
        return current_book_data.json()

    # Function to view all books in the database (incl. current book)
    def view_all_books_UI(self):
        endpoint3 = f"{self.get_base_url()}/books"
        view_all_books_data = requests.get(endpoint3)
        return view_all_books_data.json()


# user interface class
class UIClass:

    # UI class attributes
    def __init__(self, user, user_subject):
        self.user = user
        self.user_subject = ""
        self.database = UIDatabaseClass() #UIClass owns UIDatabaseClass instance

    # welcome message
    def welcome(self):
        return f'''
== == == == == == == == == == == == == == == == == == == == == == == == == == 
\U0001F4DA  Hello {self.user}, Welcome to The Blind Date with a Book Portal! \U0001F4DA
== == == == == == == == == == == == == == == == == == == == == == == == == =='''
    #unicode for book emoji is \U0001F4DA
    #unicode for calendar emoji is \U0001F4C5

    # prints main menu
    def display_options(self):
        print("Please choose from the following options: ")
        print("A: Choose a new book \U0001F4DA")
        print("B: View current book and deadline \U0001F4DA \U0001F4C5 ")
        print("C: View previous books \U0001F4DA \U0001F4DA \U0001F4DA ")

    # prints genre selection for new book
    def display_genres(self):
        print ("Please choose a genre: ")
        print ("A: Horror")
        print ("B: Comedy")
        print ("C: Romance")
        print ("D: Random genre")

if __name__ == '__main__':
    try:
        print("TESTING")

        # Create instances
        # ui_db = UIDatabaseClass()
        # ui = UIClass("Test User", "Romance")

        # Test 1: Welcome message
        # print("Test 1: Displaying welcome message...")
        # print(ui.welcome(), "\n")

        # Test 2: Display options menu
        # print("Test 2: Displaying options menu...")
        # ui.display_options()
        # print()

        # Test 3: Display genres menu
        # print("Test 3: Displaying genres menu...")
        # ui.display_genres()
        # print()

        # Test 4: View current books - Flask must be running
        # print("Test 4: Testing view current book...")
        # print(ui_db.view_current_book_UI(), "\n")

        # Test 5: View all books - Flask must be running
        # print("Test 5: Testing view all books...")
        # print(ui_db.view_all_books_UI())

        # Check base url
        # db = UIDatabaseClass()
        # print("Base URL:", db.get_base_url())
        #
        # # #try to change base url
        # db = UIDatabaseClass()
        # try:
        #     db.set_base_url("http://fake_site.com")
        # except ValueError as e:
        #     print("Unsuccessful:", e)

    except Exception as e:
        print("Unsuccessful:", e)




