# Class : Class is a blue print for creating a new object
# Object :  Instance of a class

class Point:
    def draw(self):
        print('draw')

point = Point()
print(f'Address of the Point Class Point -- > {point}')
print(f'Type of an object ---> {type(point)}')
# CHECKING the instance of the point class
print(f'Checking the Instance of an point object and Point Class -->{isinstance(point,Point)}')


# class MyPoint:
#     def __init__(self):
#         pass
#
# point = MyPoint()
# print(f'Object of a MyPoint Class {point}')
# print(f'Instance of an object {isinstance(point,MyPoint)}')