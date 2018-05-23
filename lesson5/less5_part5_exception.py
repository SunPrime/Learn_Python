class DevidedByZeroExcertion(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class A:
    def devided(self, a, b):
        if b == 0:
            raise DevidedByZeroExcertion('b is equal to zero')
        return a/b

def method():
    a = A()
    try:
        a.devided(10,0)
    except DevidedByZeroExcertion as e:
        print(e)
        raise
    except Exception as e:
        print('Exception')
    finally:
        print('finally')

try:
    method()
except DevidedByZeroExcertion as e:
    print('Next raise exception')
