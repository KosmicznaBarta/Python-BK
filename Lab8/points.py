import math
import unittest

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    # point1 == point2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # point1 != point2
    def __ne__(self, other):
        return not self == other
    
    # Wektory 2D poniżej:

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    # Iloczyn wektorowy
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    # Iloczyn skalarny
    def cross(self, other):
        return self.x * other.y - self.y * other.x
    
    # Długość wektorowa
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    # Tuple, immutable points
    def __hash__(self):
        return hash((self.x, self.y))
    

class TestPoint(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Point(2, 3)), "(2, 3)")

    def test_repr(self):
        self.assertEqual(repr(Point(2, 3)), "Point(2, 3)")

    def test_eq(self):
        self.assertTrue(Point(2, 3) == Point(2, 3))
        self.assertFalse(Point(2, 3) == Point(3, 4))

    def test_ne(self):
        self.assertTrue(Point(2, 3) != Point(3, 4))
        self.assertFalse(Point(2, 3) != Point(2, 3))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))

    def test_sub(self):
        self.assertEqual(Point(5, 7) - Point(2, 3), Point(3, 4))

    def test_mul(self):
        self.assertEqual(Point(2, 3) * Point(4, 5), 2*4 + 3*5)

    def test_cross(self):
        self.assertEqual(Point(2, 3).cross(Point(4, 5)), 2*5 - 3*4)

    def test_length(self):
        self.assertAlmostEqual(Point(3, 4).length(), 5.0)
        self.assertAlmostEqual(Point(1, 1).length(), math.sqrt(2))

    def test_hash(self):
        self.assertEqual(hash(Point(2, 3)), hash((2, 3)))
        self.assertNotEqual(hash(Point(2, 3)), hash((3, 4)))

if __name__ == "__main__":
    unittest.main()