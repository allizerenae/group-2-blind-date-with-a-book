import unittest
from unittest.mock import patch, Mock
import requests
from app.book_api import get_random_book_by_genre


# -----------------------------
# Tests for book_api
# -----------------------------
class TestBookAPI(unittest.TestCase):

    # Tests for book returned in a valid genre
    def test_valid_genre(self):
        result = get_random_book_by_genre("horror")
        # Check it returned a dictionary with book data
        self.assertIn("title", result)
        self.assertIn("author", result)
        self.assertEqual(result["genre"], "horror")

    # Tests error message for an invalid genre selection
    def test_invalid_genre(self):
        result = get_random_book_by_genre("nonsense_genre")
        self.assertEqual(result, {"ERROR": "No books found in this genre"})

    # Tests an API call error
    @patch("app.book_api.requests.get")
    def test_api_error(self, mock_get):
        mock_get.side_effect = requests.RequestException("Network failure")

        result = get_random_book_by_genre("romance")
        self.assertEqual(result, {"ERROR": "Network or API error"})

    # Tests no books available in genre from API
    @patch("app.book_api.requests.get")
    def test_empty_works_response(self, mock_get):
        # Simulate an API response with no works
        mock_response = Mock()
        mock_response.json.return_value = {"works": []}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = get_random_book_by_genre("empty_genre")
        self.assertEqual(result, {"ERROR": "No books found in this genre"})


if __name__ == "__main__":
    unittest.main()
