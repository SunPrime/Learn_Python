class Quadrangle:
    def __init__(self, line1, line2, line3, angle1, angle2):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.angle1 = angle1
        self.angle2 = angle2

    def square(self):
        return 1

class Parallelogram(Quadrangle):
    def __init__(self, line1, line2, angle):
        Quadrangle.__init__(self, line1, line2, line1, angle, 180-angle)

    def square(self):
        return 2

class Rectangle(Quadrangle):
    def __init__(self, line1, line2):
        Quadrangle.__init__(self, line1, line2, line1, 90, 90)

    def square(self):
        return 3

class Romb(Parallelogram):
    def __init__(self, line, angle):
        Parallelogram.__init__(self, line, line, angle)

    def square(self):
        return 4

class Square(Rectangle, Romb):
    def __init__(self, line):
        Rectangle.__init__(self, line, line)
        Romb.__init__(self, line, 90)


s = Square(10)
print(s.square())