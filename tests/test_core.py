import unittest

from service_library import greet


class TestGreet(unittest.TestCase):
    def test_greet_happy_path(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_empty_raises(self):
        with self.assertRaises(ValueError):
            greet("")


if __name__ == "__main__":
    unittest.main()
