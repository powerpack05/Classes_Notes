# class :blueprint for creating new objects
# object : Instance of a class

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point = Point(1, 2)
other = Point(10, 20)
print(point == other)
print(point > other)
print(point < other)
addition = point + other
print(addition)
