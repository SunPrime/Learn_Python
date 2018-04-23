#типичный пример со-процедуры
def f():
    print("f")
    yield 1
    print("f2")
    yield 2

def main():
    generator = f()
    print("ex1")
    res1 = next(generator)
    print(res1)
    res2 = next(generator)
    print(res2)

main()