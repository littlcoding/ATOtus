from src.Figure import Figure

class Rectangle(Figure):
    name = 'Rectangle'

    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError('Cannot create rectangle: all sides must be positive')

        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a*self.side_b

    def perimeter(self):
        return self.side_a*2 + self.side_b*2

    def get_rectangle_side(self):
        return [self.side_a, self.side_b]
