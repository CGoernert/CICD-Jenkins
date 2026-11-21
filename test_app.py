import unittest
from unittest.mock import patch
from app import main

class TestApp(unittest.TestCase):
    @patch("builtins.print")
    def test_main(self, mock_print):
        main()
        mock_print.assert_called_once_with("Hello, Jenkins!")

if __name__ == "__main__":
    unittest.main()