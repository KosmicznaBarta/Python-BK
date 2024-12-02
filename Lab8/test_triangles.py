import pytest
from triangles import Triangle
from points import Point

def test_init():
    with pytest.raises(ValueError, match="Punkty są współliniowe i nie tworzą trójkąta."):
        Triangle(0, 0, 1, 1, 2, 2)

def test_str():
    tr = Triangle(0, 2, 3, 4, 0, 1)
    assert str(tr) == "[(0, 2), (3, 4), (0, 1)]"

def test_repr():
    tr = Triangle(0, 0, 1, 0, 0, 1)
    assert repr(tr) == "Triangle(0, 0, 1, 0, 0, 1)"

def test_eq():
    tr1 = Triangle(0, 0, 1, 0, 0, 1)
    tr2 = Triangle(0, 1, 1, 0, 0, 0)
    assert tr1 == tr2

def test_ne():
    tr1 = Triangle(0, 0, 1, 0, 0, 1)
    tr2 = Triangle(0, 3, 1, 2, 4, 3)
    assert tr1 != tr2

def test_center():
    tr = Triangle(0, 0, 6, 0, 0, 6)
    assert tr.center == Point(2, 2)

def test_area():
    tr = Triangle(0, 0, 6, 0, 0, 6)
    assert tr.area() == 18

def test_move():
    tr = Triangle(0, 0, 1, 0, 0, 1)
    moved = tr.move(1, 1)
    assert moved == Triangle(1, 1, 2, 1, 1, 2)

def test_make4():
    tr = Triangle(0, 0, 2, 0, 0, 2)
    sub_triangles = tr.make4()
    assert len(sub_triangles) == 4
    assert all(isinstance(sub, Triangle) for sub in sub_triangles)

# Nowe metody
def test_from_points():
    points = [Point(0, 0), Point(1, 0), Point(0, 1)]
    triangle = Triangle.from_points(points)
    assert triangle.pt1 == Point(0, 0)
    assert triangle.pt2 == Point(1, 0)
    assert triangle.pt3 == Point(0, 1)

def test_bounding_box_properties():
    triangle = Triangle(0, 0, 4, 0, 0, 3)
    assert triangle.top == 3
    assert triangle.bottom == 0
    assert triangle.left == 0
    assert triangle.right == 4
    assert triangle.width == 4
    assert triangle.height == 3
    assert triangle.topleft == Point(0, 3)
    assert triangle.bottomleft == Point(0, 0)
    assert triangle.topright == Point(4, 3)
    assert triangle.bottomright == Point(4, 0)
