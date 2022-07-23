class Figure:
    name = None

    @property
    def area(self):
        pass

    @property
    def perimetr(self):
        pass

    def add_area(self, figure: 'Figure'):
        return self.area() + figure.area()
