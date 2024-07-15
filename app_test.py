from app import returnBackwardsString
import unittest

class TestApp(unittest.TestCase):
    def test_return_backwards_string(self):
        random_string = "This is my test string"
        random_string_reversed = "gnirts tset ym si sihT"
        try:
            self.assertEqual(random_string_reversed, returnBackwardsString(random_string))
        except AssertionError as e:
            print(f"AssertionError: {e}")
            raise

if __name__ == "__main__":
    unittest.main()
