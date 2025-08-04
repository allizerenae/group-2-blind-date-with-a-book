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
        return f"Welcome {self.user} to Blind Date with a Book Portal!"

    def display_options(self):
        print("Please choose from the following options: ")
        print("A: Choose a new book")
        print("B: View current book and deadline")
        print("C: View previous books")

    def option_a(self):
        # display genre options, choose genre and get a new book. Will need the API for this function.
        pass


# user interface class - interaction with database

class UIDatabaseClass:
    def add_to_book_tracker(self):
        # will call on the book class and save the book data to the database, and add a deadline
        pass

    def option_b(self):
        # function to view the current book and deadline in the database
        pass

    def option_c(self):
        # function to view previous books read in the database
        pass

def main():
    main_user = UIClass("Debbie")
    print(UIClass.welcome(main_user))
    UIClass.display_options(main_user)


if __name__ == '__main__':
    main()
