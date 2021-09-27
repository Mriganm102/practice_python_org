import unittest

from exercise2 import main

class MyTestCase(unittest.TestCase):
    def test_even(self):
        self.assertEqual(main(number="8"), "even")
    def test_odd(self):
        self.assertEqual(main(number="7"), "odd")
    def test_not_an_integer(self):
        self.assertEqual(main(number="7.5"), "not an integer")

if __name__ == '__main__':
    unittest.main()
