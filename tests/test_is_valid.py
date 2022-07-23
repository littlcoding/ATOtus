import pytest

from src.Circle import Circle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Triangle import Triangle

def test_valid_circle():
    with pytest.raises(ValueError):
        Circle(-1)


def test_valid_aquare():
    with pytest.raises(ValueError):
        Square(0)


def test_valid_rectangle():
    with pytest.raises(ValueError):
        Rectangle(side_a=0, side_b=-5)


def test_valid_triangle():
    with pytest.raises(ValueError):
        Triangle(side_a=10, side_b=1, side_c=3)
