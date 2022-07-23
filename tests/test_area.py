import math


def test_circle_area(circle_1):
    rad = circle_1.get_circle_radius()
    exp = math.pi * rad ** 2
    assert circle_1.area() == exp


def test_square_area(square_1):
    side = square_1.get_square_side()
    exp = side ** 2
    assert square_1.area() == exp


def test_rectangle_area(rectangle_1):
    sides = rectangle_1.get_rectangle_side()
    side_a = sides[0]
    side_b = sides[1]
    exp = side_b * side_a
    assert rectangle_1.area() == exp


def test_triangle_area(triangle_1):
    sides = triangle_1.get_triangle_side()
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]
    h_perimeter = (side_a + side_b + side_c) / 2
    exp = math.sqrt(h_perimeter * (h_perimeter - side_a) * (h_perimeter - side_b) * (h_perimeter - side_c))
    assert triangle_1.area() == exp
