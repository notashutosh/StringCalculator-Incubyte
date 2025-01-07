import unittest
from StringCalculator import sumOfString


class StringCalculatorTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(sumOfString(""), 0)


unittest.main()
