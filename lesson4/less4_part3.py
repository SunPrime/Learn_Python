class A(object):
    def __init__(self, a):
        self.a = a

    def method(self):
        print(self.a)

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.b = b

    def method(self):
        print(self.b)


b1 = B(10, 20)
b1.method()