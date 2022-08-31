from src.Figure import Figure
import math

class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError('Cannot create triangle: all sides must be positive')
        if side_a > (side_b+side_c):
            raise ValueError('Side_a must be less than a summ of the other sides')
        if side_b > (side_a+side_c):
            raise ValueError('Side_b must be less than a summ of the other sides')
        if side_c > (side_b+side_a):
            raise ValueError('Side_c must be less than a summ of the other sides')

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        h_perimeter = self.perimeter() / 2
        return math.sqrt(h_perimeter * (h_perimeter - self.side_a) * (h_perimeter - self.side_b) * (h_perimeter - self.side_c))

    def get_triangle_side(self):
        return [self.side_a, self.side_b, self.side_c]
