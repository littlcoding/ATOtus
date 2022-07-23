import math


def test_circle_perimeter(circle_1):
    rad = circle_1.get_circle_radius()
    exp = math.pi * rad * 2
    assert circle_1.perimeter() == exp


def test_square_perimeter(square_1):
    side = square_1.get_square_side()
    exp = side * 4
    assert square_1.perimeter() == exp


def test_rectangle_perimeter(rectangle_1):
    sides = rectangle_1.get_rectangle_side()
    side_a = sides[0]
    side_b = sides[1]
    exp = (side_b + side_a) * 2
    assert rectangle_1.perimeter() == exp


def test_triangle_perimeter(triangle_1):
    sides = triangle_1.get_triangle_side()
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]
    exp = side_a + side_b + side_c
    assert triangle_1.perimeter() == exp
