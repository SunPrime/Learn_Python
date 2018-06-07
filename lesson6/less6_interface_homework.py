def my_abstract(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper

class MetaA(type):
    abstract_metod = set()
    def __new__(cls, name, base, dict):
        print('new meta class')
        print(cls)
        print(name)
        print(base)
        print(dict)

        for key, value in dict.items():
            if value.__str__().find('my_abstract') > 0:
                cls.abstract_metod.add(key)
        print(cls.abstract_metod)

        cls.method_list = set()
        for key, value in dict.items():
            if value.__str__().find('function'):
                cls.method_list.add(key)
        print(cls.method_list)

        if cls.abstract_metod.issubset(cls.method_list):
            print('Good job!')
        else:
            print('exception')

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


class C(B):
    def method_a(self):
        pass

    def method_h(self):
        pass