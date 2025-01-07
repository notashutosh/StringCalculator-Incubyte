import unittest


class StringCalculatorTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(sumOfString(""), 0)


unittest.main()
