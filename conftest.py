import pytest

from src.Circle import Circle
from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle


@pytest.fixture
def circle_1():
    return Circle(radius=4)

@pytest.fixture
def triangle_1():
    return Triangle(side_a=3, side_b=4, side_c=5)

@pytest.fixture
def square_1():
    return Square(side=5.5)

@pytest.fixture
def rectangle_1():
    return Rectangle(side_a=4, side_b=6)

