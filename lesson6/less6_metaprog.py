class B:
    pass

def g(self, x):
    return x + 1

A = type('A', (B), {'f': lambda self, x: x + 1})
pa = A()
print(pa.f(10))
print(A.__name__)

#вариант 2
def g(self, x):
    return x + 1

def g2(self, x):
    return x * 2

A = type('A', (), {'f': g, 'h': g2})
pa = A()
print(pa.f(10))
print(pa.h(10))
print(A.__name__)

