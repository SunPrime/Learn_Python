class A:
    static_field = 10

    def f(self):
        A.static_field = 20

    @staticmethod
    def my_static_method():
        print('static method')
        print(A.static_field)

a = A()
a.static_field = 200
print(A.static_field)
print(a.__dict__)
A.static_field = 1000
print(A.static_field)
del a.__dict__['static_field']
print(a.__dict__)
A.my_static_method()