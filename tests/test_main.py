import unittest
from unittest.mock import patch, MagicMock, ANY
from main import get_valid_choice, view_books, fetch_and_save_book, handle_backend_error
from datetime import date
import requests


# -----------------------------
# Tests for get_valid_choice
# -----------------------------
class TestGetValidChoice(unittest.TestCase):

    # Class attributes for each test
    def setUp(self):
        self.prompt = "Enter your genre choice (A-D): "
        self.valid_options = ["A", "B", "C", "D"]

    # Tests a valid input
    @patch("builtins.print")
    @patch("main.input", return_value="B")
    def test_valid_input(self, mock_user_input, mock_print):
        actual = get_valid_choice(self.prompt, self.valid_options)
        self.assertEqual("B", actual)

    # Tests handling of an invalid input followed by a valid one.
    @patch("builtins.print")
    @patch("main.input", side_effect=["x", "C"])
    def test_invalid_then_valid(self, mock_user_input, mock_print):
        actual = get_valid_choice(self.prompt, self.valid_options)
        self.assertEqual("C", actual)

    # Tests handling of lowercase input
    @patch("builtins.print")
    @patch("main.input", return_value="a")
    def test_lowercase(self, mock_user_input, mock_print):
        actual = get_valid_choice(self.prompt, self.valid_options)
        self.assertEqual("A", actual)

    # Tests handling of spacing within input
    @patch("main.input", return_value=" a ")
    @patch("builtins.print")
    def test_spacing(self, mock_user_input, mock_print):
        actual = get_valid_choice(self.prompt, self.valid_options)
        self.assertEqual("A", actual)

    # Tests handling of empty input
    @patch("builtins.print")
    @patch("main.input", side_effect=["", "D"])
    def test_empty_then_valid(self, mock_user_input, mock_print):
        actual = get_valid_choice(self.prompt, self.valid_options)
        self.assertEqual("D", actual)

    # Tests handling of invalid symbol characters
    @patch("builtins.print")
    @patch("main.input", side_effect=["!", "B"])
    def test_symbol_then_valid(self, mock_user_input, mock_print):
        actual = get_valid_choice(self.prompt, self.valid_options)
        self.assertEqual("B", actual)


# -----------------------------
# Tests for view_books
# -----------------------------
class TestViewBooks(unittest.TestCase):

    # Tests handling of view current book
    @patch("builtins.print")
    def test_view_current_book(self, mock_print):
        ui_db = MagicMock()
        ui_db.view_current_book_ui = MagicMock(return_value="Current Book: Dracula")

        view_books(ui_db, "B")

        ui_db.view_current_book_ui.assert_called_once()
        mock_print.assert_any_call("\nBooks:\n")
        mock_print.assert_any_call("Current Book: Dracula")

    # Tests handling of view all books when as a list
    @patch("builtins.print")
    def test_view_all_books_list(self, mock_print):
        ui_db = MagicMock()
        ui_db.view_all_books_ui = MagicMock(return_value=["Book 1", "Book 2"])

        view_books(ui_db, "C")

        ui_db.view_all_books_ui.assert_called_once()
        mock_print.assert_any_call("\nBooks:\n")
        mock_print.assert_any_call("Book 1")
        mock_print.assert_any_call("Book 2")

    # Tests handling of view all books when empty
    @patch("builtins.print")
    def test_view_all_books_single(self, mock_print):
        ui_db = MagicMock()
        ui_db.view_all_books_ui = MagicMock(return_value="No books found.")

        view_books(ui_db, "C")

        ui_db.view_all_books_ui.assert_called_once()
        mock_print.assert_any_call("\nBooks:\n")
        mock_print.assert_any_call("No books found.")


# -----------------------------
# Tests for fetch_and_save_book
# -----------------------------

# Applying common patches for all tests in the class
@patch("main.get_valid_choice", return_value="B")
@patch("main.get_random_book_by_genre", return_value={
    "title": "Funny Book",
    "author": "Jane Doe",
    "genre": "Comedy"
})
@patch("main.get_assigned_date", return_value=date(2025, 8, 19))
@patch("main.get_deadline", return_value=date(2025, 8, 26))
class TestFetchAndSaveBook(unittest.TestCase):

    def setUp(self):
        self.ui = MagicMock()
        self.ui.user_subject = ""
        self.ui_db = MagicMock()

    # Tests genre selection and book creation
    @patch("builtins.print")
    def test_genre_and_book_saved(self, mock_print, mock_deadline, mock_assigned, mock_api, mock_choice):
        fetch_and_save_book(self.ui, self.ui_db)

        # display genres should be called
        self.ui.display_genres.assert_called_once()

        # genre mapping should be correct
        self.assertEqual(self.ui.user_subject, "Comedy")

        # check book saved to database with correct fields
        self.ui_db.add_new_book_to_database_ui.assert_called_once_with({
            "book_title": "Funny Book",
            "author": "Jane Doe",
            "genre": "Comedy",
            "assigned_date": "2025-08-19",
            "deadline": "2025-08-26"
        })

    # Tests printed messages
    @patch("builtins.print")
    def test_printed_output(self, mock_print, mock_deadline, mock_assigned, mock_api, mock_choice):
        fetch_and_save_book(self.ui, self.ui_db)
        mock_print.assert_any_call("Fetching a book from the Open Library API...")
        mock_print.assert_any_call("\nHere’s your blind date book:\n", ANY)
        mock_print.assert_any_call("Book saved to your reading list.")


# -----------------------------
# Tests for handle_backend_error
# -----------------------------
class TestHandleBackendError(unittest.TestCase):
    # Tests if there is a database connection error
    @patch("builtins.print")
    def test_connection_error(self, mock_print):
        handle_backend_error(requests.exceptions.ConnectionError())
        mock_print.assert_any_call("ERROR: Could not connect to the backend server.")
        mock_print.assert_any_call("Please make sure your Flask API is running correctly at http://127.0.0.1:5000/")
        mock_print.assert_any_call("Ensure your config file is correctly set up.")

    # Tests for any other error with the database
    @patch("builtins.print")
    def test_generic_exception(self, mock_print):
        handle_backend_error(Exception("Test error"))
        mock_print.assert_any_call("ERROR: Something went wrong while saving to the database. Details: Test error")


if __name__ == "__main__":
    unittest.main()
