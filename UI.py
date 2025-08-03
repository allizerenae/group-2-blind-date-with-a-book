# user interface classes

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
        pass # relates to function in book_api.py

# user interface class - interaction with database -
class UIDatabaseClass:
    def add_to_book_tracker(self):
        pass

    def option_b(self):
        pass

    def option_c(self):
        pass

def main():
    main_user = UIClass("Debbie")
    print(UIClass.welcome(main_user))
    UIClass.display_options(main_user)


if __name__ == '__main__':
    main()
