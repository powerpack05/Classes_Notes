# class : Class is a blueprint for creating a new object
# object : Object is a Instance of a class

class Point:
    # Defining the constructor
    """
        For Defining the constructor we use
        __init__ magic method
        self : 'self' is a reference to the current  object
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Points ({self.x},{self.y})')


point = Point(10, 20)
point.draw()
point.draw()
print(point)
