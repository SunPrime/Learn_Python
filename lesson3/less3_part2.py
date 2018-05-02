"""# lambda-фукции
s = lambda x, y: x + y
print(s(10, 20))

def map(lis,f):
    return [f(element) for element in lis]

def g(x):
    return x + 1

l=[19,20,40]
res = map(l,g)
print(res)
"""
# или пишем так
def map(lis,f):
    return [f(element) for element in lis]

l=[19,20,40]
res = map(l, lambda x: x + 1)
print(res)
