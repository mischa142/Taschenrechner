import unittest
from main import addieren, subtraktion, muliplikation, division

class test_taschenrechner(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addieren(2, 3), 5)
        self.assertEqual(addieren(-1, 1), 0)
        self.assertEqual(addieren(0, 0), 0)

    def test_subtraktion(self):
        self.assertEqual(subtraktion(3, 3), 0)
        self.assertEqual(subtraktion(-1, 1), -2)
        self.assertEqual(subtraktion(0, 0), 0)

    def test_multiplikation(self):
        self.assertEqual(multiplikation(2, 3), 6)
        self.assertEqual(multiplikation(-1, 1), -1)
        self.assertEqual(multiplikation(0, 5), 0)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(-6, 3), -2)
        self.assertEqual(division(0, 5), 0)
        with self.assertRaises(ValueError):
            division(5, 0)

if __name__ == '__main__':
    unittest.main()
