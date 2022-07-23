import math


def test_add_square_to_circle(circle_1, square_1):
    side = square_1.get_square_side()
    sq_area = side ** 2

    rad = circle_1.get_circle_radius()
    ci_area = math.pi * rad ** 2

    exp = sq_area + ci_area
    assert circle_1.add_area(square_1) == exp


def test_add_square_to_rectangle(rectangle_1, square_1):
    side = square_1.get_square_side()
    sq_area = side ** 2

    sides = rectangle_1.get_rectangle_side()
    side_a = sides[0]
    side_b = sides[1]
    re_area = side_b * side_a

    exp = sq_area + re_area
    assert rectangle_1.add_area(square_1) == exp


def test_add_square_to_triangle(triangle_1, square_1):
    side = square_1.get_square_side()
    sq_area = side ** 2

    sides = triangle_1.get_triangle_side()
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]
    h_perimeter = (side_a + side_b + side_c) / 2
    tr_area = math.sqrt(h_perimeter * (h_perimeter - side_a) * (h_perimeter - side_b) * (h_perimeter - side_c))

    exp = sq_area + tr_area
    assert triangle_1.add_area(square_1) == exp


def test_add_square_to_square(square_1):
    side = square_1.get_square_side()
    sq_area = side ** 2

    exp = sq_area * 2
    assert square_1.add_area(square_1) == exp
