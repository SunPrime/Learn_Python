class MetaA(type):
    def __new__(cls, name, base, dict):
        print('new meta class')
        print(cls)
        print(name)
        print(base)
        print(dict)
        return type.__new__(cls, name, base, dict)

    def __init__(cls, name, base, dict):
        print('Init meta class')


class A(metaclass=MetaA):
    def __new__(cls):
        print('New from A')
        return object.__new__(cls)

    def __init__(self):
        print('Init from A')

class B(A):
    def __new__(cls):
        print('New from B')
        return object.__new__(cls)

    def __init__(self):
        print('Init from B')
