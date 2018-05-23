class A:
    def __init__(self):
        print('A')

    def method(self):
        print('A')

class B:
    def __init__(self):
        print('B')

    def method(self):
        print('B')

class C(A, B):
    def __init__(self):
        super(A, self).__init__()

c = C()
c.method()
B.method(c)