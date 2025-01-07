import unittest
from StringCalculator import sumOfString


class StringCalculatorTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(sumOfString(""), 0)

    def test_nonempty(self):
        self.assertEqual(sumOfString("1"), 1)

    def test_multidigit(self):
        self.assertEqual(sumOfString("11"), 11)

    def test_comma(self):
        self.assertEqual(sumOfString("1,1"), 2)

    def test_custom_delimiter_not_newline(self):
        self.assertEqual(sumOfString("//;\n1;1"), 2)

    def test_custom_delimiter_multichar(self):
        self.assertEqual(sumOfString("//***\n1***1"), 2)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            sumOfString("-1")
        self.assertEqual(str(context.exception),
                         "negative numbers not allowed -1")

    def test_negative_numbers_multiple(self):
        with self.assertRaises(ValueError) as context:
            sumOfString("-1, -2")
        self.assertEqual(str(context.exception),
                         "negative numbers not allowed -1,-2")

    def test_negative_numbers_multiple_with_positive_numbers(self):
        with self.assertRaises(ValueError) as context:
            sumOfString("-1, 5, -3, 3")
        self.assertEqual(str(context.exception),
                         "negative numbers not allowed -1,-3")

    def test_negative_numbers_multiple_with_delimiter(self):
        with self.assertRaises(ValueError) as context:
            sumOfString("//;\n1;-2")
        self.assertEqual(str(context.exception),
                         "negative numbers not allowed -2")

    def test_ignore_superthousand(self):
        self.assertEqual(sumOfString("1001,2"), 2)

    def test_multiple_delimiters(self):
        self.assertEqual(sumOfString("//[;][***]\n1;2***3"), 6)


unittest.main()
