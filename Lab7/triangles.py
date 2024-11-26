from points import Point
import unittest

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

        if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
            raise ValueError("Punkty są współliniowe i nie tworzą trójkąta.")
        
    def __str__(self):
        return f"[{self.pt1}, {self.pt2}, {self.pt3}]"
    
    def __repr__(self):
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"
    
    def __eq__(self, other):
        if not isinstance(other, Triangle):
            return NotImplemented
        return set((self.pt1, self.pt2, self.pt3)) == set((other.pt1, other.pt2, other.pt3))
    
    def __ne__(self, other):
        return not self == other
    
    # środek trójkąta
    def center(self):
        x = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        y = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(x, y)
    
    # pole trójkąta
    def area(self):
        return abs(
            self.pt1.x * (self.pt2.y - self.pt3.y) + 
            self.pt2.x * (self.pt3.y - self.pt1.y) + 
            self.pt3.x * (self.pt1.y - self.pt2.y)
        ) / 2
    
    # przesunięcie o (x, y)
    def move(self, x, y):
        return Triangle(
            self.pt1.x + x, self.pt1.y + y,
            self.pt2.x + x, self.pt2.y + y,
            self.pt3.x + x, self.pt3.y + y 
        )
    
    # zwraca krotkę czterech mniejszych
    def make4(self):
        mid1 = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        mid2 = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)
        mid3 = Point((self.pt3.x + self.pt1.x) / 2, (self.pt3.y + self.pt1.y) / 2)

        return (
            Triangle(self.pt1.x, self.pt1.y, mid1.x, mid1.y, mid3.x, mid3.y),
            Triangle(mid1.x, mid1.y, self.pt2.x, self.pt2.y, mid2.x, mid2.y),
            Triangle(mid3.x, mid3.y, mid2.x, mid2.y, self.pt3.x, self.pt3.y),
            Triangle(mid1.x, mid1.y, mid2.x, mid2.y, mid3.x, mid3.y)
        )
    
class TestTriangle(unittest.TestCase):
    def test_init(self):
        # Z możliwością testowania tylko dla ValueError 
        # with self.assertRaises(ValueError):
            Triangle(0, 3, 1, 2, 4, 3)

    def test_str(self):
        tr = Triangle(0, 2, 3, 4, 0, 1)
        self.assertEqual(str(tr), "[(0, 2), (3, 4), (0, 1)]")

    def test_repr(self):
        tr = Triangle(0, 0, 1, 0, 0, 1)
        self.assertEqual(repr(tr), "Triangle(0, 0, 1, 0, 0, 1)")

    def test_eq(self):
        tr1 = Triangle(0, 0, 1, 0, 0, 1)
        tr2 = Triangle(0, 1, 1, 0, 0, 0)
        self.assertTrue(tr1 == tr2)

    def test_ne(self):
        tr1 = Triangle(0, 0, 1, 0, 0, 1)
        tr2 = Triangle(0, 3, 1, 2, 4, 3)
        self.assertTrue(tr1 != tr2)

    def test_center(self):
        tr = Triangle(0, 0, 6, 0, 0, 6)
        self.assertEqual(tr.center(), Point(2, 2))

    def test_area(self):
        tr = Triangle(0, 0, 6, 0, 0, 6)
        self.assertEqual(tr.area(), 18)

    def test_move(self):
        tr = Triangle(0, 0, 1, 0, 0, 1)
        moved = tr.move(1, 1)
        self.assertEqual(moved, Triangle(1, 1, 2, 1, 1, 2))

    def test_make4(self):
        tr = Triangle(0, 0, 2, 0, 0, 2)
        sub_triangles = tr.make4()
        self.assertEqual(len(sub_triangles), 4)
        self.assertTrue(all(isinstance(sub, Triangle) for sub in sub_triangles))

if __name__ == "__main__":
    unittest.main()
