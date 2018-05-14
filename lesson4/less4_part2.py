import math


class Point:
    def __init__(self, x, y):
        self.x =x
        self.y = y

class Circle(Point):
    def __init__(self, x, y, r):
        Point.__init__(self, x, y)
        self.r = r

def distance(point):
    return math.sqrt(point.x * point.x + point.y * point.y)


p = Point(10, 20)
d = distance(p)
print(d)
circle = Circle(10, 20, 100)
d = distance(circle)
print(d)