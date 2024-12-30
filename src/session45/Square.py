from src.session44.inheritance_concept import Shape


class Square(Shape):
    def __init__(self, width, height):
        Shape.__init__(self, width , height)

