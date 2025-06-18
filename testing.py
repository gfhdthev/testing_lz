import unittest
from funck import ygoreck


class TestEqualize(unittest.TestCase):
    def test_integer_positive_numbers(self):
        self.assertEqual(ygoreck(10, 2, 30, 4, 5), 2.6976)

    def test_zero_divizion(self):
        self.assertEqual(ygoreck(2, 2, 2, 2, 2), 'Деление на ноль невозможно')

    def test_float_positive_numbers(self):
        self.assertEqual(ygoreck(2.4, 6.5, 1, 2, 99.99), 1.0995)

    def test_negative_root(self):
        self.assertEqual(ygoreck(1, 2, 3, 4, -2), 'Невозможно извлечь конень из отрицательного числа')

    def test_error_input(self):
        self.assertEqual(ygoreck('asdff', 0, 4, 5, 0), 'Введенные вами значения не являются числом')
        self.assertEqual(ygoreck('', 0, 4, 5, 0), 'Введенные вами значения не являются числом')
        self.assertEqual(ygoreck('10**-9', 0, 4, 5, 0), 'Введенные вами значения не являются числом')

if __name__ == '__main__':
    unittest.main()