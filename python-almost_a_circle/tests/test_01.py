import unittest

class TestString(unittest.TestCase):
    def test_should_capitalize_string(self):
        string = "hello"
        expected_value = "Hello"
        self.assertEqual(string.capitalize(), expected_value)