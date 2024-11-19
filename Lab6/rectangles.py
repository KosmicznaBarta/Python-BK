from points import Point
import unittest

class Rectangle:
    # (x1, y1) - lewy dolny, (x2, y2) - prawy górny
    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"
    
    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"
    
    # point1 == point2
    def __eq__(self, other):
        return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)
    
    # point1 != point2
    def __ne__(self, other):
        return not self == other
    
    # Ustaw środek
    def center(self):
        center_x = (self.pt1.x + self.pt2.x) / 2
        center_y = (self.pt1.y + self.pt2.y) / 2
        return Point(center_x, center_y)
    
    # Pole
    def area(self):
        width = abs(self.pt2.x - self.pt1.x)
        height = abs(self.pt2.y - self.pt1.y)
        return width * height
    
    # Przesunięcie o wektor
    def move(self, x, y):
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(0, 0, 4, 3)
        self.rect2 = Rectangle(1, 1, 5, 4)
        self.rect3 = Rectangle(0, 0, 4, 3)

    def test_str(self):
        self.assertEqual(str(self.rect1), "[(0, 0), (4, 3)]")

    def test_repr(self):
        self.assertEqual(repr(self.rect1), "Rectangle(0, 0, 4, 3)")

    def test_eq(self):
        self.assertTrue(self.rect1 == self.rect3)
        self.assertFalse(self.rect1 == self.rect2)

    def test_ne(self):
        self.assertTrue(self.rect1 != self.rect2)
        self.assertFalse(self.rect1 != self.rect3)

    def test_center(self):
        center = self.rect1.center()
        self.assertEqual((center.x, center.y), (2, 1.5))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 12)
        self.assertEqual(self.rect2.area(), 12)

    def test_move(self):
        moved_rect = self.rect1.move(1, 1)
        self.assertEqual(moved_rect.pt1, Point(1, 1))
        self.assertEqual(moved_rect.pt2, Point(5, 4))

if __name__ == '__main__':
    unittest.main()
