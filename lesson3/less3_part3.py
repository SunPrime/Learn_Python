class A:
    def __init__(self):
        self.a = 10
        self.b = 20

pa = object.__new__(A)
A.__init__(pa)

print(pa.__dict__) #словарь значений класса, поля класса
print(A.__dict__) #словарь методов класса