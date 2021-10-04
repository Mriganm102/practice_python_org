import unittest
from exercise3 import exercise3a, exercise3c, exercise3, exercise3b

class MyTestCase(unittest.TestCase):
    def test_exercise3(self):
        self.assertEqual(exercise3(), 1)
    def test_exercise3a(self):
        self.assertEqual(exercise3a(), [1,1,2,3])
    def test_exercise3b(self):
        self.assertEqual(exercise3b(), [1,1,2,3])
    def test_exercise3c(self):
        self.assertEqual(exercise3c(b=55), [1,1,2,3,5,8,13,21,34])



if __name__ == '__main__':
    unittest.main()
