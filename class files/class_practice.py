# Class :   Class is a blueprint for creating a new object
# Object : Object is an Instance of a class

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print('Hello Deep Learning Developer')


point = Point(1,2)
point.draw()
print(point)
print(type(point))
print(isinstance(point, Point))
