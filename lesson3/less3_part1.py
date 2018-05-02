def f():
    print("ok")
    j1 = yield 1
    print('j1 = ' + str(j1))
    j2 = yield 2
    print('j2 = ' + str(j2))

g = f() #генератор
r1 = next(g)
print('r1= ' + str(r1))
r2 = g.send(10)
print('r2 = ' + str(r2))
r3 = g.send(30)