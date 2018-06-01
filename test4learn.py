l = [lambda: x * 2 for x in range(10)]
print(l)
for r in l:
    print(r())