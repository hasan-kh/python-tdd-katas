import unittest
from main import add


class TestAddMethod(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_one_number(self):
        self.assertEqual(add("5"), 5)
        self.assertEqual(add("66"), 66)

    @unittest.skip('covered')
    def test_two_numbers(self):
        self.assertEqual(add("5,4"), 9)
        self.assertEqual(add("0,3"), 3)

    def test_unknown_amount_of_numbers(self):
        self.assertEqual(add("1,1,2,3,2,5"), 14)

    def test_newline_separator(self):
        self.assertEqual(add('1,2\n3\n4,5\n6'), 21)

    def test_optional_separator(self):
        self.assertEqual(add('//;\n1;2\n3\n4'), 10)

    def test_negetive_number(self):
        with self.assertRaises(Exception) as e:
            add('1,-5')

        self.assertEqual(e.exception.args[0], 'negatives not allowed [-5]')

    def test_multiple_negatives(self):
        with self.assertRaises(Exception) as e:
            add('//*\n1*-6\n-1')

        self.assertEqual(e.exception.args[0], 'negatives not allowed [-6, -1]')

    def test_ignore_greater_than_1000(self):
        self.assertEqual(add("2,1000"), 1002)
        self.assertEqual(add("2,1001"), 2)

    def test_delimiter_with_any_length(self):
        self.assertEqual(add("//[***]\n1***2***3\n4"), 10)

    def test_multiple_delimiters_with_any_length(self):
        self.assertEqual(add("//[*][%]\n1*2%3"), 6)
        self.assertEqual(add("//[****][%%][!]\n1****2%%3!4\n5"), 15)


if __name__ == '__main__':
    unittest.main()