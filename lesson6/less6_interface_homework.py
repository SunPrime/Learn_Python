def my_abstract(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper

class MetaA(type):
    abstract_metod = []
    def __new__(cls, name, base, dict):
        print('new meta class')
        print(cls)
        print(name)
        print(base)
        print(dict)
        return type.__new__(cls, name, base, dict)


class A(metaclass=MetaA):
    @my_abstract
    def method_f(self):
        pass

    @my_abstract
    def method_g(self):
        pass

    def method_h(self):
        pass


class B(A):
    def method_f(self):
        pass

    def method_g(self):
        pass

