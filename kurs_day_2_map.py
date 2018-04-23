'''def increment(x):
    return x + 1

def map(lis, f):
#    result = []
#    for element in lis:
#        result.append(f(element))
#    return result
    return [f(element) for element in lis]

massive = [10,20,30]
result_massive = map(massive,increment)

print(result_massive)

def high_func():
    def g(a):
        return a * 2
    return g

res = high_func()
print(res(10))

#декоратор без параметров
def percents_verify(function):
    def wrapper(account, percents):
        print("wrapper")
        if percents > 30:
            percents = 30
        result = function(account,percents)
        return result
    return wrapper

@percents_verify
def ratio(account, percent):
    return account + account * percent / 100

print(ratio(100,35))'''

#декоратор с параметрами
def percents_verify(a,b):
    def external_wrapper(function):
        def wrapper(account, percents):
            print("wrapper")
            if percents < a:
                percents = 0
            if percents > b:
                percents = b
            result = function(account,percents)
            return result
        return wrapper # wrapper1
    return external_wrapper #wrapper2

@percents_verify(0,30)
def ratio(account, percent):
    return account + account * percent / 100

#new_percents = ratio(100,50)
wrapper1 = percents_verify(0,30)
wrapper2 = wrapper1(ratio)
new_percents = wrapper2(100,50)
print(new_percents)