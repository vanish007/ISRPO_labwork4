import unittest
import math

class RectangleTestCase(unittest.TestCase):
    def test_one_side_is_zero(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(-1, 0), 0)
        self.assertEqual(area(-1.5, 0), 0)
        self.assertEqual(area(1000000000039, 0), 0)

    def test_square_area(self):
        self.assertEqual(area(1, 1), 1)
        self.assertEqual(area(2, 2), 4)
        self.assertEqual(area(10, 10), 100)
        self.assertEqual(area(11, 11), 121)
        self.assertEqual(area(1000000000039, 1000000000039), 1000000000039 * 1000000000039)

    def test_rectangle_area(self):
        self.assertEqual(area(3, 4), 12)
        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(1.5, 2.5), 3.75)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4), 14)
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(1.5, 2.5), 8.0)

    def test_diagonal(self):
        self.assertAlmostEqual(diagonal(3, 4), 5.0)
        self.assertAlmostEqual(diagonal(5, 12), 13.0)
        self.assertAlmostEqual(diagonal(1.5, 2.5), math.sqrt(1.5**2 + 2.5**2))

    def test_inradius(self):
        self.assertAlmostEqual(inradius(3, 4), 3.428571, places=6)
        self.assertAlmostEqual(inradius(5, 12), 7.058824, places=6)
        self.assertAlmostEqual(inradius(1.5, 2.5), 1.875, places=6)

    def test_outradius(self):
        self.assertAlmostEqual(outradius(3, 4), 2.5)
        self.assertAlmostEqual(outradius(5, 12), 6.5)
        self.assertAlmostEqual(outradius(1.5, 2.5), math.sqrt(1.5**2 + 2.5**2) / 2)

def area(a, b):
    return a * b

def perimeter(a, b):
    return 2 * (a + b)

def diagonal(a, b):
    return math.sqrt(a**2 + b**2)

def inradius(a, b):
    semi_perimeter = (a + b) / 2
    return (a * b) / semi_perimeter if semi_perimeter != 0 else 0

def outradius(a, b):
    return math.sqrt(a**2 + b**2) / 2
