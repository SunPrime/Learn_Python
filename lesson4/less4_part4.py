class A(object):
    def __init__(self):
        self.method()

    def method(self):
        print('a')

class B(A):
    def __init__(self):
        A.__init__(self)

    def method(self):
        print('b')

b = B()
b.method()