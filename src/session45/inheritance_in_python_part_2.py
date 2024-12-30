class Shape:
    def __init__(self, width, height):
        self._width = width
        self._height = height


    def area(self):
        print("area is called")
        return self._width * self._height

    def perimeter(self):
        print("perimeter is called")
        return 2 * (self._width + self._height)

    #Method overWriting
    #This method was overWrite from Object class
    def __repr__(self):
        print("__repr__ is called in Shape class")