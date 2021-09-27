import unittest

from exercise2 import main, exercise2a

class MyTestCase(unittest.TestCase):
    def test_even(self):
        self.assertEqual(main(number="8"), "even")
    def test_odd(self):
        self.assertEqual(main(number="7"), "odd")
    def test_not_an_integer(self):
        self.assertEqual(main(number="7.5"), "not an integer")
    def test_divisible_by_four(self):
        self.assertEqual(exercise2a(number_string="8"), "divisible by 4")
    def test_is_not_divisible_by_four(self):
        self.assertEqual(exercise2a(number_string="7"), "not divisible by 4")
    def test_not_divisible_by_integer(self):
        """ Test is run in the exercise 4a series
        and isn't an integer, so it can't be
        divisible by an integer without a remainder"""
        self.assertEqual(exercise2a(number_string="8.5"), "not an integer")


if __name__ == '__main__':
    unittest.main()
