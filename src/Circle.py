from src.Figure import Figure
import math

class Circle(Figure):
    name = 'Circle'

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Cannot create circle: radius must be positive')

        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

    def perimeter(self):
        return math.pi*self.radius*2

    def get_circle_radius(self):
        return self.radius
