# Class : Class is a blueprint for creating a new object
# Object : Object is an Instance of a class
# Instance Attributes : Instance Attributes can be declared outside the class
# Class Attributes : Class Attributes can be declared after the class and can be changed using object Instance
#                    by class name

class Point:
    """
        Declaring the Class Attributes
    """
    default_colour = "red"

    """
        Declaring the Instance Attributes of Point Class
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point ({self.x},{self.y})')


point = Point(10,20) # Creating the Instance of a Point class called point object
# you can declare the instance attribute outside the class as well
point.z = 10
print(point.z)
point.draw()
print(f'Object Point {point}')
print(f'Type of the object {type(point)}')
print(f'Checking the instances of the object and Class {isinstance(point,Point)}')
print(point.default_colour)
print(Point.default_colour)

# you can declare the another Point object
another = Point(12,13)
another.draw()
another.z = 100
print(another.z)
another.default_colour = "baby pink"
print(another.default_colour)
Point.default_colour = "Rainbow"
print(Point.default_colour)

