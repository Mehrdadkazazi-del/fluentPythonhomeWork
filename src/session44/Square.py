from src.session44.inheritance_concept import Shape


class Square(Shape):
    def __init__(self, width, height):
        Shape.__init__(self, width , height)
        self.width = width
        self.height = height

    @property
    def center(self):
        return self.width / 2, self.height / 2

