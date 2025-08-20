import unittest
from unittest.mock import patch
from main import get_valid_choice

class TestGetValidChoice(unittest.TestCase):

    # class attributes for each test
    def setUp(self):
        self.prompt = "Enter your genre choice (A-D): "
        self.valid_options = ["A", "B", "C", "D"]

    # tests a valid input
    @patch("main.input", return_value="B")
    def test_valid_input(self, mock_user_input):
        actual = get_valid_choice(self.prompt, self.valid_options)
        self.assertEqual("B", actual)

    # tests handling of an invalid input followed by a valid one.
    @patch("main.input", side_effect=["x", "C"])
    def test_invalid_then_valid(self, mock_user_input):
        actual = get_valid_choice(self.prompt, self.valid_options)
        self.assertEqual("C", actual)

    # tests handling of lowercase input
    @patch("main.input", return_value="a")
    def test_lowercase(self, mock_user_input):
        actual = get_valid_choice(self.prompt, self.valid_options)
        self.assertEqual("A", actual)

    # tests handling of spacing within input
    @patch("main.input", return_value=" a ")
    def test_spacing(self, mock_user_input):
            actual = get_valid_choice(self.prompt, self.valid_options)
            self.assertEqual("A", actual)

if __name__ == "__main__":
    unittest.main()