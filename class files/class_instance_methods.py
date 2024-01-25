# class :blueprint for creating new objects
# object : Instance of a class
# self :it is a reference the current object

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f'Point ({self.x},{self.y})')


point = Point.zero()
point.draw()
