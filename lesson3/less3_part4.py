class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def square(self):
        return 3.14 * self.radius * self.radius

p=Point(10, 20)
"""print(p.x)
print(p.__dict__['x'])
p.x = 100
p.__dict__['x'] = 100"""

c = Circle(p, 100)
res = c.square()
print(res)