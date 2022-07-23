from src.Figure import Figure

class Square(Figure):
    name = 'Square'

    def __init__(self, side):
        if side <= 0:
            raise ValueError('Cannot create square: all sides must be positive')

        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side*4

    def get_square_side(self):
        return self.side
