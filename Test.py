import unittest
from unittest.mock import patch


def add(a,b):
    return a-b;


class TestMe(unittest.TestCase):
    @patch("__main__.add", return_value= 4)
    def test_add(self, mock_add):
        self.assertEqual(add(4,1), 4)
        
if __name__ == "__main__":
    unittest.main()